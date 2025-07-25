#!/Users/dbless/github/notes/bin/.benv/bin/python
# Simple Pomodoro Timer
import tkinter
from PIL import Image, ImageTk
from tkinter import ttk
import time
from enum import Enum
import os


class PomodoroTimer:
    """A simple pomodoro timer."""

    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#2a9d8f"
    YELLOW = "#f7f5dd"
    BLUE = "#1ca0f2"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 45
    TIMER_LABEL_COLORS = {
        "Timer": BLUE,
        "Work": RED,
        "Break": GREEN,
        "Long Break!": GREEN,
    }

    class RoundState(Enum):
        WORK = 0
        BREAK = 1
        LONG_BREAK = 2

    @staticmethod
    def dynamic_path(path: str) -> str:
        """Returns the path to a file relative to the script's directory."""
        return os.path.join(
            os.path.join(os.path.dirname(__file__), "assets", "pomodoro"), path
        )

    @staticmethod
    def load_image(path: str, size=(64, 64)) -> ImageTk.PhotoImage:
        """Loads an image from the assets folder and returns a resized image."""
        new_path = PomodoroTimer.dynamic_path(path)
        image = Image.open(PomodoroTimer.dynamic_path(path))
        image = image.resize(size)
        return ImageTk.PhotoImage(image)

    @staticmethod
    def time_to_string(time: int):
        minutes = int(time // 60)
        seconds = int(time % 60)
        return f"{minutes:02}:{seconds:02}"

    def __init__(self):
        # Timer in seconds
        self._timer: int = 0
        self.timer_running = False
        # Pomodoro round
        self._round = 0

        self.setup_ui()

    # ---------------------------- UI SETUP ------------------------------- #
    def setup_window(self):
        """Sets up the tkinter window in the setup ui method."""
        self.window = tkinter.Tk()
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=50, bg=self.YELLOW)

    def setup_buttons(self):
        """Sets up the buttons in the setup ui method with ttk."""
        style = ttk.Style()
        style.configure(
            "TButton",
            font=("Arial", 20),
        )

    def setup_canvas(self):
        """Sets up the canvas and tomato image in the setup ui method."""
        self.canvas = tkinter.Canvas(
            width=200, height=224, bg=self.YELLOW, highlightthickness=0
        )
        self.tomato_img = tkinter.PhotoImage(
            file=PomodoroTimer.dynamic_path("tomato.png")
        )
        self.canvas.create_image(100, 112, image=self.tomato_img)
        self.canvas.create_text(
            100,
            130,
            text="00:00",
            fill="white",
            font=(self.FONT_NAME, 35, "bold"),
            justify="center",
            tags="timer_text",
        )
        self.canvas.grid(column=1, row=1)

    @property
    def timer_label_text(self) -> str:
        return self._timer_label_text

    @timer_label_text.setter
    def timer_label_text(self, value: str):
        """Sets the timer label text and updates the timer label."""
        self._timer_label_text = value
        self.update_timer_label()

    def setup_label(self):
        # Timer Label
        self._timer_label_text = "Timer"
        self.timer_label = tkinter.Label(
            text=self.timer_label_text,
            fg=self.BLUE,
            bg=self.YELLOW,
            font=(self.FONT_NAME, 50),
        )
        self.timer_label.grid(column=1, row=0)

        # Start and Reset Buttons
        self.start_button = ttk.Button(
            self.window, text="Start", style="TButton", command=self.start_timer
        )
        self.start_button.grid(column=0, row=2)

        self.reset_button = ttk.Button(
            self.window, text="Reset", style="TButton", command=self.reset_timer
        )
        self.reset_button.grid(column=2, row=2)

    def setup_checkmarks(self):
        """Sets up the checkmarks in the setup ui method."""
        self.checkmark_frame = tkinter.Frame(self.window, name="checkmarks_frame")
        self.checkmark_frame.grid(column=1, row=3, padx=10)

    def set_checkmarks(self, number_of_checkmarks: int):
        """Sets the number of checkmarks to display."""
        self.checkmark_frame.destroy()
        self.setup_checkmarks()

        for _ in range(number_of_checkmarks):
            checkmark_label = tkinter.Label(
                self.checkmark_frame, image=self.checkmark_image, bg=self.YELLOW
            )
            checkmark_label.pack(side="left")

    def setup_ui(self):
        """Sets up the UI in the init method."""
        self.setup_window()
        self.setup_buttons()
        self.setup_canvas()
        self.setup_label()
        self.setup_checkmarks()
        self.checkmark_image = self.load_image("checkmark.png", (32, 32))

        self.window.mainloop()

    # ---------------------------- UI UPDATE ------------------------------- #
    def update_timer_text(self):
        """Updates the timer text."""
        self.canvas.itemconfig(
            "timer_text",
            text=self.time_to_string(self.timer),
        )

    def update_timer_label(self):
        """Updates the timer label."""
        if self.timer_label_text not in self.TIMER_LABEL_COLORS:
            raise ValueError(
                f"Invalid timer label text. Must be one of {self.TIMER_LABEL_COLORS.keys()}"
            )
        # Set the timer label text and color
        self.timer_label.config(
            text=self.timer_label_text,
            fg=self.TIMER_LABEL_COLORS[self.timer_label_text],
        )

    # ---------------------------- TIMER MECHANISM ------------------------------- #
    @property
    def timer(self) -> int:
        return self._timer

    @timer.setter
    def timer(self, value: int):
        self._timer = value
        self.update_timer_text()

    def start_timer(self):
        """Starts the timer if it is not already running."""
        if not self.timer_running:
            self.timer_running = True
            self.timer = self.WORK_MIN * 60
            self.timer_label_text = "Work"
            self.window.after(1000, self.countdown)

    def reset_timer(self):
        """Resets the timer."""
        self.timer_running = False
        self.timer_label_text = "Timer"
        self.timer = 0
        self.round = 0

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
    @property
    def round(self) -> int:
        return self._round

    @round.setter
    def round(self, value: int):
        self._round = value
        num_checkmarks = self._round // 2 + self._round % 2

        self.set_checkmarks(num_checkmarks)

    def countdown(self):
        """Countdown method for the timer."""
        if self.timer_running:
            if self.timer != 0:
                self.timer -= 1
                self.window.after(1000, self.countdown)

            # Finish round
            else:
                self.handle_finish_round()

    def handle_finish_round(self):
        """Handle finishing round when timer reaches 0."""
        self.round += 1

        # Switch on round state
        match self.round_to_enum(self.round):
            case self.RoundState.WORK:
                self.timer = self.WORK_MIN * 60
                self.timer_label_text = "Work"
                self.countdown()
            case self.RoundState.BREAK:
                self.timer = self.SHORT_BREAK_MIN * 60
                self.timer_label_text = "Break"
                self.countdown()
            case self.RoundState.LONG_BREAK:
                self.timer = self.LONG_BREAK_MIN * 60
                self.timer_label_text = "Long Break!"
                self.countdown()
            case _:
                raise ValueError("Invalid round state")

    @staticmethod
    def is_odd(number: int) -> bool:
        return number % 2 == 1

    @staticmethod
    def is_even(number: int) -> bool:
        return number % 2 == 0

    @staticmethod
    def is_long_break(round_number: int) -> bool:
        return round_number % 8 == 7

    @staticmethod
    def is_break(round_number: int) -> bool:
        return PomodoroTimer.is_odd(round_number) and not PomodoroTimer.is_long_break(
            round_number
        )

    @staticmethod
    def is_work(round_number: int) -> bool:
        return PomodoroTimer.is_even(round_number)

    @classmethod
    def round_to_enum(cls, round_number: int):
        """Switches the round state based on the round number."""
        if PomodoroTimer.is_work(round_number):
            return cls.RoundState.WORK
        elif PomodoroTimer.is_break(round_number):
            return cls.RoundState.BREAK
        elif PomodoroTimer.is_long_break(round_number):
            return cls.RoundState.LONG_BREAK
        else:
            raise ValueError(f"Invalid round number: {round_number}")


if __name__ == "__main__":
    print("Happy Working!")
    pomodoro_timer = PomodoroTimer()
