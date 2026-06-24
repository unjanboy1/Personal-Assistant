"""
assistant.py

Main assistant controller.
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

    def __init__(self):

        self.listener = SpeechToText()

        self.speaker = TextToSpeech()

        self.parser = CommandParser()

        self.apps = AppController()

        self.browser = BrowserController()

        self.explorer = ExplorerController()

        self.keyboard = KeyboardController()

        self.mouse = MouseController()

        self.system = SystemController()

    def execute(self, command):

        data = self.parser.parse(command)

        intent = data["intent"]

        print(data)

        if intent == "OPEN_APP":

            target = data["target"]

            if target:

                self.speaker.speak(f"Opening {target}")

                self.apps.open_app(target)

        elif intent == "SEARCH_WEB":

            query = data["query"]

            if query:

                self.speaker.speak(f"Searching {query}")

                self.browser.search_google(query)

        elif intent == "UNKNOWN":

            self.speaker.speak(
                "Sorry, I did not understand that command."
            )

    def start(self):

        self.speaker.speak("VoicePilot is ready.")

        while True:

            command = self.listener.listen()

            if not command:
                continue

            if command in ["exit", "quit", "stop"]:

                self.speaker.speak("Goodbye.")

                break

            self.execute(command)


if __name__ == "__main__":

    assistant = VoiceAssistant()

    assistant.start()