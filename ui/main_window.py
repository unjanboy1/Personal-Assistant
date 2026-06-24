"""
main_window.py

Main GUI of VoicePilot.
"""

import tkinter as tk

from ui.widgets import StatusLabel
from ui.widgets import OutputBox


class MainWindow:

    def __init__(self):

        self.root = tk.Tk()

        self.root.title("VoicePilot")

        self.root.geometry("700x550")

        self.root.resizable(False, False)

        title = tk.Label(

            self.root,

            text="VoicePilot",

            font=("Segoe UI", 24, "bold")

        )

        title.pack(pady=15)

        self.status = StatusLabel(self.root)

        self.output = OutputBox(self.root)

    def set_status(self, text):

        self.status.update(text)

    def log(self, text):

        self.output.write(text)

    def run(self):

        self.root.mainloop()


if __name__ == "__main__":

    window = MainWindow()

    window.log("VoicePilot Started")

    window.run()