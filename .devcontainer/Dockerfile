FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Download and install rerun cli
ADD https://github.com/rerun-io/rerun/releases/download/0.21.0/rerun-cli-0.21.0-x86_64-unknown-linux-gnu /usr/local/bin/rerun

# Make rerun executable
RUN chmod +x /usr/local/bin/rerun
