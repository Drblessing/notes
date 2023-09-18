# This script edits mp3 metadata.

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

# Loop over all .mp3 files in the current directory
for file in *.mp3; do
    # Extract the track number from the filename
    track_number=$(echo "$file" | cut -d'.' -f1)

    # Remove all tags
    eyeD3 --remove-all "$file"

    # Set the artist name, album name, and track number
    eyeD3 --artist="$artist" --album="$album" --track="$track_number" "$file"
    

    # Set the album art to "Album_Cover.jpg" (uncomment if needed)
    eyeD3 --add-image=Album_Cover.jpg:FRONT_COVER "$file"

    # Remove track number from prefix of filename
    # So "1. song.mp3" becomes "song.mp3"
    mv "$file" "${file#$track_number. }"
done

echo "All mp3 files have been updated!"

