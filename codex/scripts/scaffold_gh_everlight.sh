#!/usr/bin/env bash
set -euo pipefail

# ------------------------------------------------------------
# gh-everlight EXTENSION SCAFFOLDER
# Creates a script-based GH CLI extension bound to a GitHub App.
#
# Requirements: gh, jq, openssl, git
# Usage:
#   ./scaffold_gh_everlight.sh \
#       -o EverLightOrg \
#       -r everlightos \
#       -a 123456 \
#       -k /path/to/your-app-private-key.pem \
#       [-H github.com] \
#       [--no-push]
#
# After it runs:
#   gh everlight auth        # fetches & caches an installation token
#   gh everlight status      # org-wide PR/issue glance
#   gh everlight init        # stub: place bootstrap logic here
# ------------------------------------------------------------

OWNER=""
TARGET_REPO=""
APP_ID=""
APP_KEY=""
GH_HOST="github.com"
PUSH_REMOTE=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--owner) OWNER="$2"; shift 2;;
    -r|--repo) TARGET_REPO="$2"; shift 2;;
    -a|--app-id) APP_ID="$2"; shift 2;;
    -k|--app-key) APP_KEY="$2"; shift 2;;
    -H|--host) GH_HOST="$2"; shift 2;;
    --no-push) PUSH_REMOTE=0; shift 1;;
    -h|--help)
      sed -n '1,60p' "$0"; exit 0;;
    *) echo "Unknown arg: $1"; exit 1;;
  esac
done

if [[ -z "$OWNER" || -z "$TARGET_REPO" || -z "$APP_ID" || -z "$APP_KEY" ]]; then
  echo "Missing required args. Run with -h for help."
  exit 1
fi

# deps check
for cmd in gh jq openssl git; do
  command -v "$cmd" >/dev/null 2>&1 || { echo "Missing dependency: $cmd"; exit 1; }
done

EXT_NAME="gh-everlight"
ROOT_DIR="$EXT_NAME"

if [[ -d "$ROOT_DIR" ]]; then
  echo "Directory $ROOT_DIR already exists. Aborting to avoid overwrite."
  exit 1
fi

mkdir -p "$ROOT_DIR"/{bin,.everlight,docs}
cat > "$ROOT_DIR/README.md" <<EOF
# $EXT_NAME

Script-based GitHub CLI extension for EverLight OS flows.

## Commands

- \`gh everlight auth\`   – Exchange GitHub App credentials for an installation token
- \`gh everlight status\` – Quick glance across PRs/issues
- \`gh everlight init\`   – Bootstrap repo/org settings (stub)

## App Binding

This extension authenticates via a GitHub App (JWT → installation token) against:
- Owner: \`${OWNER}\`
- Repo:  \`${TARGET_REPO}\`
- Host:  \`${GH_HOST}\`
EOF

cat > "$ROOT_DIR/.gitignore" <<'EOF'
.everlight/token.json
.everlight/jwt.txt
.env.local
EOF

# --- helper: base64url in POSIX-y way
cat > "$ROOT_DIR/bin/base64url.sh" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
# stdin -> base64url(no padding)
openssl base64 -A | tr '+/' '-_' | tr -d '='
EOF
chmod +x "$ROOT_DIR/bin/base64url.sh"

# --- main extension executable (must match repo name, no extension)
cat > "$ROOT_DIR/gh-everlight" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

SELF_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CACHE_DIR="$(cd "$SELF_DIR" && cd .everlight && pwd 2>/dev/null || echo "$SELF_DIR/.everlight")"

OWNER="{{OWNER}}"
TARGET_REPO="{{TARGET_REPO}}"
APP_ID="{{APP_ID}}"
APP_KEY_PATH="{{APP_KEY_PATH}}"
GH_HOST="{{GH_HOST}}"

B64URL="$SELF_DIR/bin/base64url.sh"
TOKEN_CACHE="$CACHE_DIR/token.json"

usage() {
  cat <<USAGE
EverLight OS – gh extension

Usage:
  gh everlight auth          Authenticate via GitHub App → installation token
  gh everlight status        Show open PRs/issues across the owner
  gh everlight init          Bootstrap repo/org configuration (stub)
  gh everlight help          This help
USAGE
}

ensure_files() {
  mkdir -p "$CACHE_DIR"
  if [[ ! -f "$APP_KEY_PATH" ]]; then
    echo "❌ App private key not found at: $APP_KEY_PATH"
    exit 1
  fi
}

now_epoch() { date +%s; }

make_jwt() {
  local iat exp header payload unsigned signed
  iat=$(( $(now_epoch) - 60 ))
  exp=$(( $(now_epoch) + 540 ))

  header='{"alg":"RS256","typ":"JWT"}'
  payload=$(jq -nc --argjson iat "$iat" --argjson exp "$exp" --arg iss "$APP_ID" '{iat:$iat, exp:$exp, iss:$iss}')

  unsigned="$(printf '%s' "$header" | "$B64URL").$(printf '%s' "$payload" | "$B64URL")"
  signed="$(printf '%s' "$unsigned" | openssl dgst -sha256 -sign "$APP_KEY_PATH" -binary | "$B64URL")"
  printf '%s.%s\n' "$unsigned" "$signed"
}

get_installation_id() {
  # Prefer repo-level installation discovery
  local jwt="$1"
  local url="https://api.${GH_HOST}/repos/${OWNER}/${TARGET_REPO}/installation"
  local resp
  resp=$(curl -fsSL -H "Authorization: Bearer ${jwt}" -H "Accept: application/vnd.github+json" "$url")
  echo "$resp" | jq -r '.id'
}

issue_installation_token() {
  local inst_id="$1" jwt="$2"
  local url="https://api.${GH_HOST}/app/installations/${inst_id}/access_tokens"
  curl -fsSL -X POST -H "Authorization: Bearer ${jwt}" -H "Accept: application/vnd.github+json" "$url"
}

write_token_cache() {
  printf '%s' "$1" > "$TOKEN_CACHE"
}

read_cached_token() {
  [[ -f "$TOKEN_CACHE" ]] || { echo "{}"; return; }
  cat "$TOKEN_CACHE"
}

token_is_valid() {
  local tok_json="$1"
  local exp_ts
  exp_ts=$(echo "$tok_json" | jq -r '.expires_at' 2>/dev/null || echo "")
  [[ -z "$exp_ts" || "$exp_ts" == "null" ]] && return 1
  local exp_epoch now
  exp_epoch=$(date -d "$exp_ts" +%s)
  now=$(now_epoch)
  # refresh if < 120s to expiry
  (( exp_epoch - now > 120 ))
}

ensure_token() {
  ensure_files
  local cached new jwt inst_id tok_json
  cached="$(read_cached_token)"
  if token_is_valid "$cached"; then
    echo "$cached"
    return 0
  fi
  jwt="$(make_jwt)"
  inst_id="$(get_installation_id "$jwt")"
  if [[ -z "$inst_id" || "$inst_id" == "null" ]]; then
    echo "❌ Could not resolve installation id. Is the app installed on ${OWNER}/${TARGET_REPO}?" >&2
    exit 1
  fi
  tok_json="$(issue_installation_token "$inst_id" "$jwt")"
  write_token_cache "$tok_json"
  echo "$tok_json"
}

with_token_env() {
  local tok_json token
  tok_json="$(ensure_token)"
  token="$(echo "$tok_json" | jq -r '.token')"
  if [[ -z "$token" || "$token" == "null" ]]; then
    echo "❌ Failed to obtain installation token"; exit 1
  fi
  GH_TOKEN="$token" GITHUB_TOKEN="$token" GITHUB_AUTH_TOKEN="$token" "$@"
}

cmd_auth() {
  local t
  t="$(ensure_token | jq -r '.token')"
  echo "✅ Installation token cached at ${TOKEN_CACHE}"
  # Optionally log the app/installation
  with_token_env gh api -H "Accept: application/vnd.github+json" "/repos/${OWNER}/${TARGET_REPO}" >/dev/null \
    && echo "🔐 Verified access to ${OWNER}/${TARGET_REPO} via GitHub App."
}

cmd_status() {
  # simple org-wide glance
  with_token_env gh search prs --owner "$OWNER" --state open --limit 20 --json title,number,repository,author,state,url \
    | jq -r '.[] | "PR #\(.number) [\(.repository.name)]: \(.title) – \(.author.login)\n\(.url)\n"'
  echo "----"
  with_token_env gh search issues --owner "$OWNER" --state open --limit 20 --json title,number,repository,author,state,url \
    | jq -r '.[] | "Issue #\(.number) [\(.repository.name)]: \(.title) – \(.author.login)\n\(.url)\n"'
}

cmd_init() {
  # stub bootstrap: create labels on target repo
  echo "🛠 Bootstrapping labels on ${OWNER}/${TARGET_REPO}..."
  with_token_env gh label create "type:feature" -R "${OWNER}/${TARGET_REPO}" --color 0E8A16 --description "New feature" 2>/dev/null || true
  with_token_env gh label create "type:bug"     -R "${OWNER}/${TARGET_REPO}" --color D73A4A --description "Bug fix"     2>/dev/null || true
  with_token_env gh label create "priority:P1"  -R "${OWNER}/${TARGET_REPO}" --color B60205 --description "Highest"     2>/dev/null || true
  echo "✅ Labels ensured."

  # place your org/repo protection, secrets, CODEOWNERS, etc. here.
  # examples (commented):
  # with_token_env gh api -X PUT "/repos/${OWNER}/${TARGET_REPO}/branches/main/protection" -f required_status_checks.strict=true ...
}

main() {
  case "${1:-help}" in
    help|-h|--help) usage;;
    auth)   shift; cmd_auth "$@";;
    status) shift; cmd_status "$@";;
    init)   shift; cmd_init "$@";;
    *) usage; exit 1;;
  esac
}

# Fill placeholders at scaffold time — do not edit below in runtime script
: <<'PLACEHOLDERS'
OWNER_PLACEHOLDER
TARGET_REPO_PLACEHOLDER
APP_ID_PLACEHOLDER
APP_KEY_PATH_PLACEHOLDER
GH_HOST_PLACEHOLDER
PLACEHOLDERS

main "$@"
EOF
chmod +x "$ROOT_DIR/gh-everlight"

# inject runtime values into the executable
safe_sed() {
  # works on GNU/BSD
  local pattern="$1" replacement="$2" file="$3"
  perl -0777 -pe "s/\Q${pattern}\E/${replacement}/g" -i "$file"
}

safe_sed "{{OWNER}}" "$OWNER" "$ROOT_DIR/gh-everlight"
safe_sed "{{TARGET_REPO}}" "$TARGET_REPO" "$ROOT_DIR/gh-everlight"
safe_sed "{{APP_ID}}" "$APP_ID" "$ROOT_DIR/gh-everlight"
safe_sed "{{APP_KEY_PATH}}" "$APP_KEY" "$ROOT_DIR/gh-everlight"
safe_sed "{{GH_HOST}}" "$GH_HOST" "$ROOT_DIR/gh-everlight"

# minimal docs
cat > "$ROOT_DIR/docs/USAGE.md" <<EOF
# gh everlight – usage

Authenticate via the GitHub App installed on ${OWNER}/${TARGET_REPO}:

\`\`\`bash
gh everlight auth
\`\`\`

Glance across open PRs/issues in ${OWNER}:

\`\`\`bash
gh everlight status
\`\`\`

Bootstrap labels on ${OWNER}/${TARGET_REPO} (extend as needed):

\`\`\`bash
gh everlight init
\`\`\`
EOF

# initialize repo & (optionally) publish
pushd "$ROOT_DIR" >/dev/null

git init -q
git add .
git commit -m "feat: initial gh-everlight extension scaffold (App auth + status + init)"

# try to create/push a remote extension repo named gh-everlight
if [[ $PUSH_REMOTE -eq 1 ]]; then
  if gh repo view "$OWNER/$EXT_NAME" --hostname "$GH_HOST" >/dev/null 2>&1; then
    echo "🔗 Remote $OWNER/$EXT_NAME exists. Setting as origin."
    git remote add origin "https://${GH_HOST}/${OWNER}/${EXT_NAME}.git" || true
  else
    echo "🚀 Creating remote repo $OWNER/$EXT_NAME on $GH_HOST..."
    gh repo create "$OWNER/$EXT_NAME" --public --source . --push --hostname "$GH_HOST"
  fi
else
  echo "↪ Skipping remote create/push (--no-push)."
fi

# install the extension locally from the working tree
echo "🧩 Installing extension locally…"
gh extension install .

popd >/dev/null

echo
echo "✅ Done. Try:"
echo "   gh everlight auth"
echo "   gh everlight status"
echo "   gh everlight init"
