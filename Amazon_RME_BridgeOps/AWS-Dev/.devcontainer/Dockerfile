# Simple Dockerfile for AWS-Dev devcontainer
FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Install common packages
COPY library-scripts /tmp/library-scripts
RUN apt-get update \
  && apt-get install -y --no-install-recommends curl unzip ca-certificates gnupg lsb-release \
  && /bin/bash /tmp/library-scripts/install-tools.sh \
  && rm -rf /var/lib/apt/lists/* /tmp/library-scripts

USER vscode
