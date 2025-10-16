chmod +x scaffold_gh_everlight.sh

./scaffold_gh_everlight.sh \
  -o EverLightOrg \
  -r everlightos \
  -a 123456 \
  -k /secure/keys/everlight-gh-app.pem


Notes & next steps

Make sure your GitHub App is installed on EverLightOrg/everlightos (or at least on the org). The script discovers the installation ID from /repos/{owner}/{repo}/installation.

The extension caches the installation token at .everlight/token.json and auto-refreshes before expiry (~1 hour tokens; refresh with gh everlight auth or just run any command).

Drop your real bootstrap logic inside cmd_init (branch protections, CODEOWNERS, org secrets, default labels, repo templates, etc.).

Want subcommands? Just add new cmd_<name> functions and a case branch (e.g., sync, kb, release, etc.).
