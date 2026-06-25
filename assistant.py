"""
assistant.py

VoicePilot Main Controller
"""

from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech

from ai.command_parser import CommandParser

from automation.apps import AppController
from automation.browser import BrowserController
from automation.explorer import ExplorerController
from automation.keyboard import KeyboardController
from automation.mouse import MouseController
from automation.system import SystemController


class VoiceAssistant:

    def __init__(self, callback=None):

        self.listener = SpeechToText()
        self.speaker = TextToSpeech()

        self.parser = CommandParser()

        self.apps = AppController()
        self.browser = BrowserController()
        self.explorer = ExplorerController()
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.system = SystemController()

        self.callback = callback

    # --------------------------------------------------------

    def update(self, message):

        print(message)

        if self.callback:
            self.callback(message)

    # --------------------------------------------------------

    def execute(self, command):

        data = self.parser.parse(command)

        print(data)

        intent = data["intent"]

        self.update(f"Command : {command}")

        # ----------------------------------------------------
        # OPEN APPLICATION
        # ----------------------------------------------------

        if intent == "OPEN_APP":

            target = data["target"]

            if target:

                self.update(f"Opening {target}")

                self.speaker.speak(f"Opening {target}")

                self.apps.open_app(target)

        # ----------------------------------------------------
        # GOOGLE SEARCH
        # ----------------------------------------------------

        elif intent == "SEARCH_WEB":

            query = data["query"]

            if query:

                self.update(f"Searching Google for {query}")

                self.speaker.speak(f"Searching {query}")

                self.browser.search_google(query)

        # ----------------------------------------------------
        # OPEN DRIVE
        # ----------------------------------------------------

        elif intent == "OPEN_DRIVE":

            drive = data["target"]

            if drive:

                self.update(f"Opening {drive} drive")

                self.speaker.speak(f"Opening {drive} drive")

                self.explorer.open_drive(drive)

        # ----------------------------------------------------
        # OPEN FOLDER
        # ----------------------------------------------------

        elif intent == "OPEN_FOLDER":

            folder = data["target"]

            if folder:

                self.update(f"Opening {folder}")

                self.explorer.open_folder(folder)

        # ----------------------------------------------------
        # BRIGHTNESS
        # ----------------------------------------------------

        elif intent == "BRIGHTNESS":

            action = data["action"]

            if action == "increase":

                self.update("Increasing Brightness")

                self.speaker.speak("Increasing Brightness")

                self.system.increase_brightness()

            elif action == "decrease":

                self.update("Decreasing Brightness")

                self.speaker.speak("Decreasing Brightness")

                self.system.decrease_brightness()

            elif action == "maximum":

                self.system.set_brightness(100)

            elif action == "minimum":

                self.system.set_brightness(0)

        # ----------------------------------------------------
        # SCREENSHOT
        # ----------------------------------------------------

        elif intent == "SCREENSHOT":

            self.update("Taking Screenshot")

            self.speaker.speak("Taking Screenshot")

            self.system.screenshot()

        # ----------------------------------------------------
        # LOCK
        # ----------------------------------------------------

        elif intent == "LOCK":

            self.update("Locking Computer")

            self.speaker.speak("Locking Computer")

            self.system.lock()

        # ----------------------------------------------------
        # KEYBOARD
        # ----------------------------------------------------

        elif intent == "TYPE":

            text = data["text"]

            if text:

                self.update(f"Typing : {text}")

                self.keyboard.type_text(text)

        # ----------------------------------------------------
        # MOUSE
        # ----------------------------------------------------

        elif intent == "MOUSE":

            action = data["action"]

            if action == "click":

                self.mouse.click()

            elif action == "double":

                self.mouse.double_click()

            elif action == "right":

                self.mouse.right_click()

        # ----------------------------------------------------

        else:

            self.update("Unknown Command")

            self.speaker.speak(
                "Sorry, I did not understand."
            )

    # --------------------------------------------------------

    def start(self):

        self.speaker.speak("VoicePilot Started")

        while True:

            self.update("Listening...")

            command = self.listener.listen()

            if not command:
                continue

            if command.lower() in ["exit", "quit", "stop"]:

                self.speaker.speak("Goodbye")

                break

            self.execute(command)


if __name__ == "__main__":

    assistant = VoiceAssistant()

    assistant.start()