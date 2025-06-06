#!/bin/bash
# Install .benv for bin scripts
# Run from any directory

# Store original directory
ORIGINAL_DIR=$(pwd)

# Navigate to notes/bin
cd ~/Github/notes/bin

# Remove .benv if it already exists
if [ -d ".benv" ]; then
    echo "Removing existing .benv directory..."
    rm -rf .benv
fi

# Install python there using homebrew python
python3 -m venv .benv

# Activate the virtual environment
source .benv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Navigate back to the original directory
cd "$ORIGINAL_DIR"