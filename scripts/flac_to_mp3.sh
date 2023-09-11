# This script converts FLAC files to MP3 format
for file in *.flac; do
    # Convert each FLAC file to MP3 format
    ffmpeg -i "$file" -ab 256k -id3v2_version 3 "${file%.flac}.mp3"
done
