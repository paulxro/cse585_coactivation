#!/bin/bash

set -Eeuo pipefail

# Update packages and install pip, python venv
sudo apt update
sudo apt install python3-pip
sudo pip install --upgrade pip
sudo apt install python3.10-venv

cd /local/repository

# Install needed extensions for vscode
chmod +x /local/repository/scripts/extensions.sh

sudo python3 -m venv env
source env/bin/activate

pip install jupyterlab
pip install torch
pip install transformers

