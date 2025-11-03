#!/usr/bin/env bash
set -euxo pipefail
for i in 1 2 3; do
  apt-get update && break || { echo "apt-get update failed; retry in 5s"; sleep 5; }
done
apt-get install -y --no-install-recommends ca-certificates curl unzip gnupg lsb-release
rm -rf /var/lib/apt/lists/*
