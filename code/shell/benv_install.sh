#!/bin/bash
# Install .benv for bin scripts

# Error handling
set -euo pipefail

# Remove existing .benv
rm -rf ~/Github/notes/bin/.benv

# Install python 
python3 -m venv ~/Github/notes/bin/.benv

# Activate the virtual environment
source ~/Github/notes/bin/.benv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r ~/Github/notes/bin/requirements_tracked.txt