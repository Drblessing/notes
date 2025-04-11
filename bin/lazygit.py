#!$HOME/Github/notes/bin/.benv/bin/python
# Lazy Git
# A python script that runs `git add .`, `git commit -m "Lazy Git Commit"`, and `git push` in one command. Useful for quickly committing changes to a repo.

# 1. Get funny commit message from whatthecommit, add default message if it fails
# 2. Pull from remote to make sure we're up to date
# 3. Add all files to staging
# 4. Commit with funny message
# 5. Push to remote

# Install libraries.
import sys
import subprocess
import importlib
import random
import requests
import argparse
from termcolor import colored


class LazyGit:
    # 1. Get funny commit message from whatthecommit list, add default message if it fails, as a property
    # Class property
    COMMIT_MESSAGES_MAIN = "https://raw.githubusercontent.com/ngerakines/commitment/main/commit_messages.txt"
    DEFAULT_COMMIT_MESSAGE = "Lazy Git Commit"
    CENSOR_LIST = [
        "shit",
        "fucking",
        "damn",
        "god",
        "dare",
        "ass",
        "bastard",
        "hell",
        "pussy",
        "prick",
        "kill",
        "cock",
        "penis",
        "vagina",
        "cunt",
        "bitch",
        "slut",
        "whore",
        "mother",
        "father",
        "bull",
        "asshole",
        "motherfucker",
    ]

    def __init__(self, commit_message: str | None = None):
        args = self.parse_args()
        self.override_commit_message = args.message
        self.args = args

    def show_changed_files(self):
        """Show changed files"""
        LazyGit.run_command(
            [
                "git",
                "diff",
                "--name-only",
            ]
        )
        LazyGit.run_command(
            [
                "git",
                "ls-files",
                "--others",
                "--exclude-standard",
            ]
        )

    @staticmethod
    def print_rainbow_text(text: str) -> None:
        """Return text in rainbow colors"""
        colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
        rainbow_text_str = ""

        for i in range(len(text)):
            # Choose the next color in the colors list
            color = colors[i % len(colors)]
            # Colorize the next character
            rainbow_text_str += colored(text[i], color)
        print(rainbow_text_str)
        return

    def parse_args(self):
        """Parse arguments"""
        parser = argparse.ArgumentParser(
            description="A python script that runs `git add .`, `git commit -m <random funny git message>`, and `git push` in one command. Useful for quickly committing changes to a repo."
        )
        parser.add_argument(
            "-m",
            "--message",
            type=str,
            help="Override Commit message with custom message",
        )

        parser.add_argument(
            "--version",
            "-v",
            action="version",
            version="%(prog)s 1.0",
            help="Show program's version number and exit.",
        )

        parser.add_argument(
            "--changes",
            "-c",
            action="store_true",
            help="Show changed files",
        )

        args = parser.parse_args()

        return args

    @classmethod
    def get_commit_message_from_url(cls, url: str = None) -> str:
        """Fetch a commit message from the URL, filtering out any with censored words."""
        # Use the default URL if none is provided.
        if url is None:
            url = cls.COMMIT_MESSAGES_MAIN

        try:
            response = requests.get(url)
            response.raise_for_status()
            # Split the fetched text into a list of non-empty, stripped messages.
            messages = [
                msg.strip() for msg in response.text.splitlines() if msg.strip()
            ]

            # Loop until we find a message that does not contain any censored words.
            while messages:
                commit_message = random.choice(messages)
                lower_message = commit_message.lower()
                # If any word in the censor list is found in the commit message,
                # remove this message from the list and try another one.
                if any(bad_word in lower_message for bad_word in cls.CENSOR_LIST):
                    messages.remove(commit_message)
                    continue
                # A valid commit message was found.
                return commit_message

            # If no valid message is found, return the default commit message.
            return cls.DEFAULT_COMMIT_MESSAGE

        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            return cls.DEFAULT_COMMIT_MESSAGE

    def get_commit_message(self) -> str:
        """Return the commit message from an override, from the fetched URL, or the default."""
        commit_message = (
            self.override_commit_message
            or self.get_commit_message_from_url()
            or self.DEFAULT_COMMIT_MESSAGE
        )
        return commit_message

    # 2. Pull from remote to make sure we're up to date
    @staticmethod
    def run_command(command: list[str]):
        """Run a command and handle errors"""
        try:
            subprocess.check_call(command)
        except subprocess.CalledProcessError as e:
            print(
                f"Command '{' '.join(command)}' failed with error code {e.returncode}"
            )
            sys.exit(1)

    @staticmethod
    def pull_from_remote():
        """Pull from remote to make sure we're up to date"""
        LazyGit.run_command(["git", "pull"])

    # 3. Add all files to staging
    @staticmethod
    def add_all_files_to_staging():
        """Add all files to staging"""
        LazyGit.run_command(["git", "add", "-A"])

    # 4. Commit with funny message
    def commit_with_funny_message(self):
        """Commit with funny message"""
        commit_message = self.get_commit_message()
        # Make some terminal whitepsace and print commit message
        # Print one line of whitepsace
        print("\n" * 1)
        self.print_rainbow_text(commit_message)
        print("\n" * 1)
        LazyGit.run_command(["git", "commit", "-m", commit_message])

    # 5. Push to remote
    @staticmethod
    def push_to_remote():
        """Push to remote"""
        LazyGit.run_command(["git", "push"])

    # 6. Run all commands
    def run_all_commands(self):
        """Run all commands"""
        self.print_rainbow_text("Lazy Git")

        if self.args.changes:
            self.show_changed_files()
        else:
            self.pull_from_remote()
            self.add_all_files_to_staging()
            self.commit_with_funny_message()
            self.push_to_remote()

        self.print_rainbow_text("Done!")


if __name__ == "__main__":
    lazygit = LazyGit()
    lazygit.run_all_commands()
