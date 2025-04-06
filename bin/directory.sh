#!/bin/bash
# Print the size of all visible and hidden subdirectories and files in the current directory, sorted by size.
# Fix no .* matches error by making a temporary hidden file.
temp_file=$(mktemp .hiddenXXXXXX)

# Use grep to filter out the temporary file from the du output
du -sh .[^.]* * 2>/dev/null | grep -v "$temp_file" | sort -h

# Clean up
rm "$temp_file"