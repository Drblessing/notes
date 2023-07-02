for file in *.opus
do
  ffmpeg -i "$file" -acodec libmp3lame -ab 128k "${file%.opus}.mp3"
done
