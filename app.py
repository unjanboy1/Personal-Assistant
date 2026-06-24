import threading

from assistant import VoiceAssistant
from ui.main_window import MainWindow


class VoicePilotApp:

    def __init__(self):

        self.gui = MainWindow()

        self.assistant = VoiceAssistant(
            callback=self.gui.log
        )

    def run_assistant(self):

        self.assistant.start()

    def run(self):

        thread = threading.Thread(
            target=self.run_assistant,
            daemon=True
        )

        thread.start()

        self.gui.run()


if __name__ == "__main__":

    app = VoicePilotApp()

    app.run()