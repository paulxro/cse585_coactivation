#!/bin/bash

set -Eeuo pipefail

declare -a extensions=(
    "ms-toolsai.jupyter"
    "ms-python.python"
    "ms-python.debugpy"
    "ms-toolsai.vscode-jupyter-cell-tags"
    "ms-toolsai.jupyter-renderers"
    "ms-toolsai.vscode-jupyter-slideshow"
    "ms-python.vscode-pylance"
    "ms-toolsai.jupyter-keymap"
)

for i in "${extensions[@]}"
do
   code --install-extension "$i"
done