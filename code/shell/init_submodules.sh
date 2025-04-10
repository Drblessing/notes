#!bin/bash
# Clone the submodules already added to the repository

# Store current directory
current_dir=$(pwd)

# Navigate to the repository directory
cd ~/Github/notes

# Initialize and update all submodules recursively
git submodule update --init --recursive

# Verify submodules were properly initialized
echo "Submodules initialized. Current status:"
git submodule status

echo "Submodule initialization complete!"