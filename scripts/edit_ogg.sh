#!/bin/bash

# This script edits ogg metadata.

# Check if enough arguments are provided
if [[ $# -lt 4 ]]; then
    echo "Usage: $0 --artist 'Artist Name' --album 'Album Name'"
    exit 1
fi

# Parse command-line arguments for artist and album
while [[ "$#" -gt 0 ]]; do
    case $1 in
        --artist) artist="$2"; shift ;;
        --album) album="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Loop over all .ogg files in the current directory
for file in *.ogg; do
    # Extract the track number from the filename
    track_number=$(echo "$file" | cut -d'.' -f1)

    # Remove all tags
    vorbiscomment -w -c /dev/null "$file"

    # Set the artist name, album name, and track number
    vorbiscomment -a -t "ARTIST=$artist" "$file"
    vorbiscomment -a -t "ALBUM=$album" "$file"
    vorbiscomment -a -t "TRACKNUMBER=$track_number" "$file"

    # Note: Setting album art in OGG files is a bit more involved and isn't handled by vorbiscomment directly. 
    # You'd need other tools or scripts for that purpose. Hence, that step is omitted here.

    # Remove track number from prefix of filename
    # So "1. song.ogg" becomes "song.ogg"
    mv "$file" "${file#$track_number. }"
done

echo "All ogg files have been updated!"
