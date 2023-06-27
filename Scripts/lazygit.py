#!/usr/bin/env python3
# Lazy Git
# A python script that runs `git add .`, `git commit -m "Lazy Git Commit"`, and `git push` in one command. Useful for quickly committing changes to a repo.

# 1. Get funny commit message from whatthecommit, add default message if it fails
# 2. Pull from remote to make sure we're up to date
# 3. Add all files to staging
# 4. Commit with funny message
# 5. Push to remote

# Import libraries
import random
import subprocess
import requests
import sys
import argparse
from termcolor import colored


class LazyGit:
    # 1. Get funny commit message from whatthecommit, add default message if it fails, as a property
    # Class property
    COMMIT_MESSAGES_MAIN = "https://raw.githubusercontent.com/Drblessing/notes/master/References/commit_messages.txt"
    COMMIT_MESSAGES_FALLBACK = "https://raw.githubusercontent.com/ngerakines/commitment/main/commit_messages.txt"
    DEFAULT_COMMIT_MESSAGE = "Lazy Git Commit"

    def __init__(self, commit_message: str | None = None):
        args = self.parse_args()
        self.override_commit_message = args.message

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

        args = parser.parse_args()

        return args

    @classmethod
    def get_commit_message_from_url(cls, url: str = COMMIT_MESSAGES_MAIN) -> str | None:
        """Get commit message from url"""
        try:
            r = requests.get(url)
            r.raise_for_status()
            text = r.text
            text = text.split("\n")
            # Get random commit message from text
            commit_message = random.choice(text)
            return commit_message

        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            return

    def get_commit_message(self) -> str:
        """Get commit message"""
        commit_message = (
            self.override_commit_message
            or self.get_commit_message_from_url()
            or self.get_commit_message_from_url(self.COMMIT_MESSAGES_FALLBACK)
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
        LazyGit.run_command(["git", "add", "."])

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
        self.pull_from_remote()
        self.add_all_files_to_staging()
        self.commit_with_funny_message()
        self.push_to_remote()
        print("Done!")


if __name__ == "__main__":
    lazygit = LazyGit()
    lazygit.run_all_commands()
