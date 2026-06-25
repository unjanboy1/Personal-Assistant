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

    # --------------------------------------------------

    def update(self, message):

        print(message)

        if self.callback:
            self.callback(message)

    # --------------------------------------------------

    def execute(self, command):

        data = self.parser.parse(command)

        print(data)

        intent = data["intent"]

        self.update(f"Command : {command}")

        # ======================================================
        # OPEN APPLICATION
        # ======================================================

        if intent == "OPEN_APP":

            target = data["target"]

            if target:

                self.update(f"Opening {target}")

                self.speaker.speak(f"Opening {target}")

                self.apps.open_app(target)

            return

        # ======================================================
        # SEARCH GOOGLE
        # ======================================================

        elif intent == "SEARCH_WEB":

            query = data["query"]

            if query:

                self.update(f"Searching Google for {query}")

                self.speaker.speak(f"Searching {query}")

                self.browser.search_google(query)

            return

        # ======================================================
        # OPEN DRIVE
        # ======================================================

        elif intent == "OPEN_DRIVE":

            drive = data["target"]

            if drive:

                self.update(f"Opening {drive} Drive")

                self.speaker.speak(f"Opening {drive} Drive")

                self.explorer.open_drive(drive)

            else:

                self.update("Please specify the drive.")

            return

        # ======================================================
        # OPEN FOLDER
        # ======================================================

        elif intent == "OPEN_FOLDER":

            folder = data["target"]

            if folder:

                self.update(f"Opening {folder}")

                self.speaker.speak(f"Opening folder")

                self.explorer.open_folder(folder)

            return

        # ======================================================
        # BRIGHTNESS
        # ======================================================

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

                self.update("Maximum Brightness")

                self.system.set_brightness(100)

            elif action == "minimum":

                self.update("Minimum Brightness")

                self.system.set_brightness(0)

            return

        # ======================================================
        # SCREENSHOT
        # ======================================================

        elif intent == "SCREENSHOT":

            self.update("Taking Screenshot")

            self.speaker.speak("Taking Screenshot")

            self.system.screenshot()

            return

        # ======================================================
        # LOCK COMPUTER
        # ======================================================

        elif intent == "LOCK":

            self.update("Locking Computer")

            self.speaker.speak("Locking Computer")

            self.system.lock()

            return
        # ======================================================
        # KEYBOARD
        # ======================================================

        elif intent == "KEYBOARD":

            action = data["action"]

            if action == "copy":

                self.update("Copy")

                self.speaker.speak("Copy")

                self.keyboard.copy()

            elif action == "paste":

                self.update("Paste")

                self.speaker.speak("Paste")

                self.keyboard.paste()

            elif action == "cut":

                self.update("Cut")

                self.speaker.speak("Cut")

                self.keyboard.cut()

            elif action == "undo":

                self.update("Undo")

                self.speaker.speak("Undo")

                self.keyboard.undo()

            elif action == "select_all":

                self.update("Select All")

                self.speaker.speak("Select All")

                self.keyboard.select_all()

            elif action == "press":

                key = data["target"]

                if key:

                    self.update(f"Pressing {key}")

                    self.speaker.speak(f"Pressing {key}")

                    self.keyboard.press_key(key)

            return

        # ======================================================
        # TYPE TEXT
        # ======================================================

        elif intent == "TYPE":

            text = data["text"]

            if text:

                self.update(f"Typing : {text}")

                self.speaker.speak("Typing")

                self.keyboard.type_text(text)

            return

        # ======================================================
        # MOUSE
        # ======================================================

        elif intent == "MOUSE":

            action = data["action"]

            if action == "click":

                self.update("Mouse Click")

                self.mouse.click()

            elif action == "double":

                self.update("Double Click")

                self.mouse.double_click()

            elif action == "right":

                self.update("Right Click")

                self.mouse.right_click()

            return

        # ======================================================
        # UNKNOWN
        # ======================================================

        else:

            self.update("Unknown Command")

            self.speaker.speak("Sorry, I did not understand.")

    # ==========================================================
    # START ASSISTANT
    # ==========================================================

    def start(self):

        self.update("VoicePilot Started")

        self.speaker.speak("VoicePilot Started")

        while True:

            self.update("Listening...")

            command = self.listener.listen()

            if not command:

                continue

            command = command.strip()

            if command == "":

                continue

            if command.lower() in [

                "exit",
                "quit",
                "stop",
                "goodbye"

            ]:

                self.update("Stopping VoicePilot")

                self.speaker.speak("Goodbye")

                break

            self.execute(command)


if __name__ == "__main__":

    assistant = VoiceAssistant()

    assistant.start()