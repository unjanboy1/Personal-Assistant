"""
assistant.py

Main VoicePilot Controller
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

        # GUI callback
        self.callback = callback

    # ------------------------------

    def update(self, message):

        print(message)

        if self.callback:
            self.callback(message)

    # ------------------------------

    def execute(self, command):

        data = self.parser.parse(command)

        intent = data["intent"]

        self.update(f"Command : {command}")

        if intent == "OPEN_APP":

            target = data["target"]

            if target:

                self.update(f"Opening {target}")

                self.speaker.speak(f"Opening {target}")

                self.apps.open_app(target)

        elif intent == "SEARCH_WEB":

            query = data["query"]

            if query:

                self.update(f"Searching Google : {query}")

                self.speaker.speak(f"Searching {query}")

                self.browser.search_google(query)

        else:

            self.update("Unknown Command")

            self.speaker.speak(
                "Sorry, I did not understand."
            )

    # ------------------------------

    def start(self):

        self.speaker.speak("VoicePilot Started")

        while True:

            self.update("Listening...")

            command = self.listener.listen()

            if command == "":
                continue

            if command in ["exit", "quit", "stop"]:

                self.speaker.speak("Goodbye")

                break

            self.execute(command)