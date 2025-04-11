import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box  # Provides various box styles
import os  # For clearing the console

console = Console()


def clear_console():
    # Clear the console screen
    os.system("cls" if os.name == "nt" else "clear")


clear_console()


def get_rainbow_ascii_art(text: str) -> Text:
    # Generate large ASCII art text.
    ascii_art = pyfiglet.figlet_format(text)
    lines = ascii_art.splitlines()

    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    rainbow_text = Text()

    for line in lines:
        for i, char in enumerate(line):
            # Preserve spaces as is.
            if char.isspace():
                rainbow_text.append(char)
            else:
                # Cycle through colors based on the character index.
                color = colors[i % len(colors)]
                rainbow_text.append(char, style=color)
        rainbow_text.append("\n")
    return rainbow_text


# Generate the rainbow ASCII art.
rainbow_art = get_rainbow_ascii_art("Lazy Git")

# Create a panel that wraps the rainbow art.
panel = Panel(
    rainbow_art,
    border_style="green",
    padding=(1, 4),  # Vertical, horizontal padding
    box=box.ROUNDED,  # A double-lined border for a thicker look
)

console.print(panel)
