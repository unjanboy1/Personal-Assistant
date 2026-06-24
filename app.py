"""
app.py

Main entry point for VoicePilot.
"""

import threading

from assistant import VoiceAssistant
from ui.main_window import MainWindow


class VoicePilotApp:

    def __init__(self):

        self.gui = MainWindow()

        self.assistant = VoiceAssistant()

    def start_assistant(self):

        self.gui.set_status("Listening...")

        self.gui.log("VoicePilot Started")

        self.assistant.start()

    def run(self):

        assistant_thread = threading.Thread(
            target=self.start_assistant,
            daemon=True
        )

        assistant_thread.start()

        self.gui.run()


if __name__ == "__main__":

    app = VoicePilotApp()

    app.run()