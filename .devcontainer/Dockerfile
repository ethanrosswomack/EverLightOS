# .devcontainer/Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

# (Optional) Set consistent locale/timezone if your tools need it
# RUN apt-get update && apt-get install -y --no-install-recommends locales tzdata && \
#     locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8

# Hardened apt install with retries; run your tools script if you use devcontainer "features" style scripts
COPY library-scripts /tmp/library-scripts
RUN set -euxo pipefail \
 && chmod +x /tmp/library-scripts/*.sh || true \
 && for i in 1 2 3; do \
      apt-get update && break || (echo "apt-get update failed; retrying in 5s" && sleep 5); \
    done \
 && apt-get install -y --no-install-recommends \
      ca-certificates \
      curl \
      unzip \
      gnupg \
      lsb-release \
 && /bin/bash /tmp/library-scripts/install-tools.sh || true \
 && rm -rf /var/lib/apt/lists/* /tmp/library-scripts
