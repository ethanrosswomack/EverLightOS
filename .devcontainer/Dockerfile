# .devcontainer/Dockerfile
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN set -euxo pipefail \
    && for i in 1 2 3; do \
         apt-get update && break || (echo "apt-get update failed, retrying in 5s..." && sleep 5); \
       done \
    && apt-get install -y --no-install-recommends \
         ca-certificates \
         curl \
         unzip \
         gnupg \
         lsb-release \
    && rm -rf /var/lib/apt/lists/*

