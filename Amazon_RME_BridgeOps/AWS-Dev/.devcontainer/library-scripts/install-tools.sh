#!/usr/bin/env bash
set -euo pipefail

echo "Installing AWS CLI v2..."
if ! command -v aws >/dev/null 2>&1; then
  curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o /tmp/awscliv2.zip
  unzip -q /tmp/awscliv2.zip -d /tmp
  /tmp/aws/install --update
  rm -rf /tmp/aws /tmp/awscliv2.zip
else
  echo "aws already installed"
fi

echo "Installing Terraform..."
if ! command -v terraform >/dev/null 2>&1; then
  TERRAFORM_VERSION="1.6.7"
  curl -sSL "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip" -o /tmp/terraform.zip
  unzip -q /tmp/terraform.zip -d /usr/local/bin
  chmod +x /usr/local/bin/terraform
  rm -f /tmp/terraform.zip
else
  echo "terraform already installed"
fi

echo "Installing AWS CDK (npm)..."
if ! command -v cdk >/dev/null 2>&1; then
  if ! command -v npm >/dev/null 2>&1; then
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get install -y nodejs
  fi
  npm install -g aws-cdk
else
  echo "cdk already installed"
fi

echo "Installing amazonq CLI (if available)..."
echo "Installing amazonq CLI via npm (preferred)..."
if ! command -v amazonq >/dev/null 2>&1; then
  # Ensure npm/node present
  if ! command -v npm >/dev/null 2>&1; then
    echo "npm not found; installing Node.js 18.x (provides npm)..."
    curl -fsSL https://deb.nodesource.com/setup_18.x | bash -
    apt-get update && apt-get install -y nodejs
  fi

  echo "Installing amazonq from npm (global)..."
  # Use --no-audit/--no-fund to keep install output concise in CI; allow failure without breaking container build
  npm install -g amazonq --no-audit --no-fund || true

  if command -v amazonq >/dev/null 2>&1; then
    echo "amazonq installed: $(amazonq --version 2>&1 | head -n1)"
  else
    echo "amazonq install failed or package not available via npm; you can update this script with an alternate install method."
  fi
else
  echo "amazonq already installed"
fi

# Clean up
apt-get autoremove -y

exit 0
