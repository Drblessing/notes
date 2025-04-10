#!/bin/bash
# Install .benv for bin scripts
# Run from any directory

# Store original directory
ORIGINAL_DIR=$(pwd)

# Navigate to notes/bin
cd ~/Github/notes/bin

# Install python there using homebrew python
python3 -m venv .benv

# Activate the virtual environment
source .benv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Deactivate the virtual environment
deactivate

# Navigate back to the original directory
cd "$ORIGINAL_DIR"