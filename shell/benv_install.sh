#!/bin/bash
# Install .benv for bin scripts

# Remove existing .benv
rm -rf ~/github/notes/bin/.benv

# Install python 
python3 -m venv ~/github/notes/bin/.benv

# Activate the virtual environment
source ~/github/notes/bin/.benv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r ~/github/notes/bin/requirements_tracked.txt