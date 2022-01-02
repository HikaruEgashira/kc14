# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.209.6/containers/python-3/.devcontainer/base.Dockerfile

ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# install pyflow
# RUN TEMP_DEB="$(mktemp)" && \
#     wget -O "$TEMP_DEB" 'https://github.com/David-OConnor/pyflow/releases/download/0.3.1/pyflow_0.3.1_amd64.deb' && \
#     dpkg -i "$TEMP_DEB" && \
#     rm -f "$TEMP_DEB"

# install
COPY /.config/* /tmp/config/
RUN sh /tmp/config/install.sh && rm -r /tmp/config

USER vscode
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /home/vscode/.local/bin/poetry config virtualenvs.in-project true
