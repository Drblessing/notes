#!$HOME/Github/notes/bin/.benv/bin/python
"""
Lazy Git
A quick Python script to run:
  git pull
  git add --all
  git commit -m "<funny commit message>"
  git push
in a single command.
"""

# Install libraries.
import sys
import subprocess
import random
import requests
import argparse
from termcolor import colored
import os


class LazyGit:
    COMMIT_MESSAGES_MAIN = "https://raw.githubusercontent.com/ngerakines/commitment/main/commit_messages.txt"
    DEFAULT_COMMIT_MESSAGE = "Lazy Git Commit"
    CENSOR_LIST = [
        "shit",
        "fuck",
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
        "Wubbalubbadubdub!",
    ]

    def __init__(self):
        args = self.parse_args()
        self.override_commit_message = args.message
        self.sync_mode = args.sync

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
            version="%(prog)s 1.2",
            help="Show program's version number and exit.",
        )

        parser.add_argument(
            "--sync",
            "-s",
            action="store_true",
            help="Sync all branches from origin, checking for local changes",
        )

        return parser.parse_args()

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
                message = random.choice(messages)
                if not cls.isCensoredMessage(message):
                    return message

                # Remove the censored message from the list.
                messages.remove(message)

            # If no valid message is found, return the default commit message.
            return cls.DEFAULT_COMMIT_MESSAGE

        except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
            return cls.DEFAULT_COMMIT_MESSAGE

        # Excpet any other error
        except Exception as e:
            return cls.DEFAULT_COMMIT_MESSAGE

    def get_commit_message(self) -> str:
        """Return the commit message from an override, from the fetched URL, or the default."""
        return self.override_commit_message or self.get_commit_message_from_url()

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
        LazyGit.run_command(["git", "pull", "--quiet"])

    @staticmethod
    def add_all_files_to_staging():
        """Add all files to staging"""
        LazyGit.run_command(["git", "add", "--all"])

    def commit(self):
        commit_message = self.get_commit_message()
        # Make some terminal whitepsace and print commit message
        # Print one line of whitepsace
        print()
        self.print_rainbow_text(commit_message)
        print()
        LazyGit.run_command(["git", "commit", "--quiet", "-m", commit_message])

    @staticmethod
    def push_to_remote():
        """Push to remote"""
        LazyGit.run_command(["git", "push", "--quiet"])

    def sync_branches(self):
        """Sync all branches from origin"""
        # Fetch all branches
        print(colored("Fetching all branches...", "cyan"))
        self.run_command(["git", "fetch", "--all"])

        # Then pull all branches
        print(colored("Pulling all branches...", "cyan"))
        self.run_command(["git", "pull", "--all"])

    def run(self):
        """Run all commands"""
        self.clear_console()
        self.print_rainbow_text("Lazy Git")

        # If sync mode is enabled, run sync first
        if self.sync_mode:
            self.sync_branches()
            return

        self.pull_from_remote()
        self.add_all_files_to_staging()
        self.commit()
        self.push_to_remote()
        self.print_rainbow_text("Done!")

    # Helper functions
    @staticmethod
    def clear_console():
        """Clear the console"""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def isCensoredMessage(message: str) -> bool:
        """Check if the message is censored"""
        for word in LazyGit.CENSOR_LIST:
            if word.lower() in message.lower():
                return True
        return False

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


if __name__ == "__main__":
    lazygit = LazyGit()
    lazygit.run()
