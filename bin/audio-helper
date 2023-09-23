#!/usr/bin/env python3
# Audio Helper
# This script is used to help with audio files.
# For now, it'll convert ogg files to mp3 files,
# and fix metadata for mp3 files.

import os
import sys
from pathlib import Path
import shutil
from mutagen.easyid3 import EasyID3
from mutagen.oggvorbis import OggVorbis
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
from pydub import AudioSegment
import logging


class AudioHelper:
    """Audio Helper.
    Handles mp3 and ogg files.
    """

    def __init__(self, path: str):
        """Initialize the Audio Helper."""
        # Set the path for the .ogg directory.
        self.path = path
        self.delete_txt_files(self.path)
        self.convert_ogg_to_mp3(self.path)
        self.format_filesystem(self.path)

    def delete_txt_files(self, path: Path):
        """Delete all .txt files in the path."""
        # Get all .txt files in the path.
        txt_files = [
            file for file in path.iterdir() if file.is_file() and file.suffix == ".txt"
        ]
        # Delete all .txt files.
        for txt_file in txt_files:
            logging.debug(f"Deleting: {txt_file}")
            txt_file.unlink()

    def convert_ogg_to_mp3(self, path: Path):
        """Convert all .ogg files in the path to .mp3 files."""

        # Fix logging
        l = logging.getLogger("pydub.converter")
        l.setLevel(logging.WARNING)

        # Verify same artist and album
        artists = set()
        albums = set()

        # Get all .ogg files in the path.
        ogg_files = [
            file
            for file in self._path.iterdir()
            if file.is_file() and file.suffix == ".ogg"
        ]
        # Convert all .ogg files to .mp3 files.
        for ogg_file in ogg_files:
            logging.debug(f"Converting: {ogg_file}")
            # Get the name of the file without the extension.
            # This will be used for the mp3 file name.
            mp3_file_name = ogg_file.parent / (ogg_file.stem + ".mp3")
            # Load the ogg file.
            ogg_audio = AudioSegment.from_ogg(ogg_file)
            # Export the ogg file as an mp3 file.
            ogg_audio.export(mp3_file_name, format="mp3", bitrate="256k")
            # Check if the mp3 file was created.
            if not mp3_file_name.is_file():
                msg = f"Failed to create mp3 file: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)
            # Verify the mp3 file bitrate.
            mp3_audio = MP3(mp3_file_name)
            if mp3_audio.info.bitrate != 256000:  # type: ignore
                msg = f"mp3 file bitrate is not 256k: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)

            # Get ogg metadata.
            ogg_metadata = OggVorbis(ogg_file)
            song_title = ogg_metadata["title"][0]
            song_artist = ogg_metadata["artist"][0]
            song_album = ogg_metadata["album"][0]
            song_track_number = ogg_metadata["tracknumber"][0]
            artists.add(song_artist)
            albums.add(song_album)
            if len(artists) > 1:
                msg = f"Artists are not the same: {artists}"
                logging.error(msg)
                raise ValueError(msg)

            if len(albums) > 1:
                msg = f"Albums are not the same: {albums}"
                logging.error(msg)
                raise ValueError(msg)

            # Delete mp3 metadata.
            mp3_metadata = EasyID3(mp3_file_name)
            mp3_metadata.delete()

            # Set mp3 metadata.
            mp3_metadata["title"] = song_title
            mp3_metadata["artist"] = song_artist
            mp3_metadata["album"] = song_album
            mp3_metadata["tracknumber"] = song_track_number
            # TODO Genere
            mp3_metadata.save()

            # Set mp3 album art, with file AlbumArt.jpg
            album_art_file = self.path / "AlbumArt.jpg"
            mp3_audio = MP3(mp3_file_name, ID3=ID3)
            mp3_audio.tags.add(
                APIC(
                    encoding=3,  # 3 is for utf-8
                    mime="image/jpeg",  # image/jpeg or image/png
                    type=3,  # 3 is for the cover image
                    desc="Cover",
                    data=open(album_art_file, "rb").read(),
                )
            )
            mp3_audio.save()
            # Verify the mp3 file metadata.
            mp3_metadata = EasyID3(mp3_file_name)
            if mp3_metadata["title"][0] != song_title:
                msg = f"mp3 file title is not the same: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)
            if mp3_metadata["artist"][0] != song_artist:
                msg = f"mp3 file artist is not the same: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)
            if mp3_metadata["album"][0] != song_album:
                msg = f"mp3 file album is not the same: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)
            if mp3_metadata["tracknumber"][0] != song_track_number:
                msg = f"mp3 file tracknumber is not the same: {mp3_file_name}"
                logging.error(msg)
                raise ValueError(msg)
            logging.debug(f"mp3 file metadata is correct: {mp3_file_name}")

            # Log the mp3 file.
            logging.info(f"Converted song: {song_title} - {song_artist} - {song_album}")

            # Create new file names.
            new_ogg_filename = song_title + ".ogg"
            new_mp3_filename = new_ogg_filename.replace(".ogg", ".mp3")
            # Rename the files.
            ogg_file.rename(self.path / new_ogg_filename)
            mp3_file_name.rename(self.path / new_mp3_filename)
        # Log the number of songs converted.
        logging.info(f"Converted {len(ogg_files)} songs.")
        self.number_of_songs = len(ogg_files)
        # Set artist and album name.
        artist_name = artists.pop()
        album_name = albums.pop()
        self.artist = artist_name.strip()
        self.album = album_name.strip()

    def format_filesystem(self, path: Path):
        """Moves mp3 and ogg files to new directories."""

        # Create new directories based on album name.
        # Get path parent directory.
        parent_dir = path.parent
        # Create new directories string.
        new_mp3_dir = parent_dir / f"{self.album} - mp3"
        new_ogg_dir = parent_dir / f"{self.album} - ogg"
        # Create new directories.
        new_mp3_dir.mkdir()
        new_ogg_dir.mkdir()
        # Move mp3 and ogg files to new directories.
        # Get all .ogg files in the path.
        ogg_files = [
            file
            for file in self._path.iterdir()
            if file.is_file() and file.suffix == ".ogg"
        ]
        # Move all .ogg files to the new directory.
        for ogg_file in ogg_files:
            logging.debug(f"Moving: {ogg_file}")
            ogg_file.rename(new_ogg_dir / ogg_file.name)
        # Copy AlbumArt.jpg to the new directory.
        album_art_file = self.path / "AlbumArt.jpg"
        shutil.copy(album_art_file, new_ogg_dir / "AlbumArt.jpg")
        # Get all .mp3 files in the path.
        mp3_files = [
            file
            for file in self._path.iterdir()
            if file.is_file() and file.suffix == ".mp3"
        ]
        # Move all .mp3 files to the new directory.
        for mp3_file in mp3_files:
            logging.debug(f"Moving: {mp3_file}")
            mp3_file.rename(new_mp3_dir / mp3_file.name)
        # Move AlbumArt.jpg to the new directory, emptying it.
        album_art_file.rename(new_mp3_dir / "AlbumArt.jpg")
        # Verify the new directories have the same number of files.
        if len(list(new_mp3_dir.iterdir())) != len(list(new_ogg_dir.iterdir())):
            msg = f"New directories do not have the same number of files."
            logging.error(msg)
            raise ValueError(msg)
        # Verify the have all the songs.
        if len(list(new_mp3_dir.iterdir())) - 1 != self.number_of_songs:
            msg = f"New directories do not have all the songs."
            logging.error(msg)
            raise ValueError(msg)

        # Delete the old emptry directory.
        self.path.rmdir()

    @property
    def path(self) -> Path:
        return self._path

    @path.setter
    def path(self, path: str):
        """Set the path for the .ogg directory.
        Validates the path.
        Coverts the path to a Path object."""
        # Convert the path str to a Path object.
        self._path = Path(path)
        # Validate the path.
        # Check it's a directory that exists.
        if not self._path.is_dir():
            msg = f"Path is not a directory: {self._path}"
            logging.error(msg)
            raise ValueError(msg)
        logging.debug(f"Path exists: {self._path}")

        # Check if the path has .ogg files.
        ogg_files = [
            file
            for file in self._path.iterdir()
            if file.is_file() and file.suffix == ".ogg"
        ]
        if len(ogg_files) == 0:
            msg = f"No .ogg files found in path: {self._path}"
            logging.error(msg)
            raise ValueError(msg)

        for ogg_file in ogg_files:
            logging.debug(f"Found ogg file: {ogg_file}")

        # Verify the path has a AlbumArt.jpg file.
        album_art_file = self._path / "AlbumArt.jpg"
        if not album_art_file.is_file():
            msg = f"AlbumArt.jpg file not found in path: {self._path}"
            logging.error(msg)
            raise ValueError(msg)
        logging.debug(f"Found AlbumArt.jpg file: {album_art_file}")


def setup_logging():
    """Setup logging for the application."""

    # Get the cwd of this file.
    cwd = Path(__file__).parent
    # Create a path to the log file.
    log_file = cwd / "logs" / "audio-helper.log"
    # Configure root logger with a file handler.
    # Also, my preferred log format and level.
    # Overwrite the log file each time the file is run.
    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        # format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s",
        format="%(message)s",
        datefmt="%m/%d/%Y %I:%M:%S %p",
        filemode="w",
    )
    # Optionaly add a console handler.
    # This will print to the console in addition to the log file.
    # Useful for debugging.
    log_console = True
    if log_console:
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        logging.getLogger("").addHandler(console)
        # Format for console logging.
        # This is different than the format for the log file.
        formatter = logging.Formatter(
            "%(filename)s:%(lineno)d - %(levelname)s - %(message)s"
        )
        console.setFormatter(formatter)

    # Start logging.
    logging.info("Started Audio Helper.")


if __name__ == "__main__":
    setup_logging()
    a = AudioHelper("")
