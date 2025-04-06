#!/bin/bash
# Print the size of all visible and hidden subdirectories and files in the current directory, sorted by size.
# Fix no .* matches error by making a temprorary hidden file.
temp_file=$(mktemp .hiddenXXXXXX)
du -sh .[^.]* * | sort -h
rm "$temp_file"