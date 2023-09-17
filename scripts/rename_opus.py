import os
import re


def cleanup_filename(filename):
    # Remove all contents within square and round brackets
    cleaned_name = re.sub(r"\[.*?\]", "", filename)
    cleaned_name = re.sub(r"\(.*?\)", "", cleaned_name)

    # Extract the track number, if any
    track_number_match = re.match(r"^(\d+\.)", cleaned_name)
    if track_number_match:
        track_number = track_number_match.group(1)
    else:
        track_number = ""

    # Remove leading zeros from the track number
    track_number = re.sub(r"^0+", "", track_number)

    # Remove leading and trailing whitespace
    cleaned_name = cleaned_name.strip()

    # Extract the song name after the dash
    song_name_match = re.search(r"- (.*)\.ogg$", cleaned_name)
    if song_name_match:
        song_name = song_name_match.group(1).strip()
    else:
        song_name = cleaned_name

    return f"{track_number} {song_name}.ogg".strip()


def main():
    # Iterate over all files in the current directory
    for original_file in os.listdir():
        if original_file.endswith(".ogg"):
            new_file = cleanup_filename(original_file)

            # Check if the new filename is valid (not empty)
            if not new_file:
                print(
                    f"Error processing: {original_file}. Resulting filename would be empty."
                )
                continue

            # Rename the file if names differ
            if original_file != new_file:
                os.rename(original_file, new_file)
                print(f"Renamed: {original_file} -> {new_file}")

    print("File names have been cleaned up!")


if __name__ == "__main__":
    main()
