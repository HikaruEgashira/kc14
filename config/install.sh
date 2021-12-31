#!/usr/bin/env bash


# https://gist.github.com/jarrodldavis/928c90036273a557848f4c73d5d4e701
# https://github.com/microsoft/vscode-dev-containers/blob/v0.122.1/containers/debian-10-git/.devcontainer/Dockerfile


USERNAME=vscode
# USER_UID=1000
# USER_GID=$USER_UID

# INSTALL_ZSH="true"
# UPGRADE_PACKAGES="true"
# COMMON_SCRIPT_SOURCE="https://raw.githubusercontent.com/microsoft/vscode-dev-containers/v0.122.1/script-library/common-debian.sh"
# COMMON_SCRIPT_SHA="da956c699ebef75d3d37d50569b5fbd75d6363e90b3f5d228807cff1f7fa211c"


# Configure apt and install packages
apt-get update
export DEBIAN_FRONTEND=noninteractive


# Verify git, common tools / libs installed, add/modify non-root user, optionally install zsh
# apt-get -y install --no-install-recommends curl ca-certificates 2>&1
# curl -sSL  ${COMMON_SCRIPT_SOURCE} -o /tmp/common-setup.sh
# ([ "${COMMON_SCRIPT_SHA}" = "dev-mode" ] || (echo "${COMMON_SCRIPT_SHA} */tmp/common-setup.sh" | sha256sum -c -))
# /bin/bash /tmp/common-setup.sh "${INSTALL_ZSH}" "${USERNAME}" "${USER_UID}" "${USER_GID}" "${UPGRADE_PACKAGES}"
# rm /tmp/common-setup.sh


# Install starship prompt
curl -fsSL https://starship.rs/install.sh | bash -s -- --yes

# Install zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-autosuggestions /home/$USERNAME/.zsh/zsh-autosuggestions

# Copy configs
cp -r /tmp/config/. /home/$USERNAME


# Clean up
apt-get autoremove -y
apt-get clean -y
rm -rf /var/lib/apt/lists/*
