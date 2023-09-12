# This script converts OGG files to MP3 format.
for file in *.ogg; do
    # Convert each OGG file to MP3 format
    ffmpeg -i "$file" -ab 256k -id3v2_version 3 "${file%.ogg}.mp3"
done
