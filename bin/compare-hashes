#!/bin/bash
# Compares the keccak-256sum of two files.

# Check if both input files are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <file1> <file2>"
  exit 1
fi

# Assign input file names to variables
file1="$1"
file2="$2"

# Check if the input files exist
if [ ! -f "$file1" ] || [ ! -f "$file2" ]; then
  echo "One or both input files do not exist."
  exit 1
fi

# Calculate keccak-256sum for each file
sha256sum "$file1" 
sha256sum "$file2" 
