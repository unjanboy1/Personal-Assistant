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

import subprocess
import psutil


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

    def open_camera(self):

        try:

            subprocess.Popen("start microsoft.windows.camera:", shell=True)

            self.update("Camera Opened")

        except Exception as e:

            print(e)

    # --------------------------------------------------

    def close_camera(self):

        for proc in psutil.process_iter():

            try:

                if proc.name().lower() in [

                    "windowscamera.exe",
                    "camera.exe"

                ]:

                    proc.kill()

            except Exception:

                pass

    # --------------------------------------------------

    def execute(self, command):

        data = self.parser.parse(command)

        print(data)

        intent = data["intent"]

        self.update(f"Command : {command}")

        # ===============================================
        # OPEN APPLICATION
        # ===============================================

        if intent == "OPEN_APP":

            target = data["target"]

            if target:

                self.update(f"Opening {target}")

                self.speaker.speak(f"Opening {target}")

                self.apps.open_app(target)

            return

        # ===============================================
        # CLOSE APPLICATION
        # ===============================================

        elif intent == "CLOSE_APP":

            target = data["target"]

            if target:

                self.update(f"Closing {target}")

                self.speaker.speak(f"Closing {target}")

                self.apps.close_app(target)

            return

        # ===============================================
        # GOOGLE SEARCH
        # ===============================================

        elif intent == "SEARCH_WEB":

            query = data["query"]

            if query:

                self.update(f"Searching {query}")

                self.speaker.speak(f"Searching {query}")

                self.browser.search_google(query)

            return

        # ===============================================
        # DRIVE
        # ===============================================

        elif intent == "OPEN_DRIVE":

            drive = data["target"]

            if drive:

                self.update(f"Opening {drive} Drive")

                self.speaker.speak(f"Opening {drive} Drive")

                self.explorer.open_drive(drive)

            return

        # ===============================================
        # FOLDER
        # ===============================================

        elif intent == "OPEN_FOLDER":

            folder = data["target"]

            if folder:

                self.update(f"Opening {folder}")

                self.speaker.speak("Opening folder")

                self.explorer.open_folder(folder)

            return

        # ===============================================
        # CAMERA
        # ===============================================

        elif intent == "OPEN_CAMERA":

            self.update("Opening Camera")

            self.speaker.speak("Opening Camera")

            self.open_camera()

            return

        elif intent == "CLOSE_CAMERA":

            self.update("Closing Camera")

            self.speaker.speak("Closing Camera")

            self.close_camera()

            return

        # ===============================================
        # BRIGHTNESS
        # ===============================================

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

            return
        # ===============================================
        # VOLUME
        # ===============================================

        elif intent == "VOLUME":

            action = data["action"]

            if action == "increase":

                self.update("Increasing Volume")

                self.speaker.speak("Increasing Volume")

                self.system.increase_volume()

            elif action == "decrease":

                self.update("Decreasing Volume")

                self.speaker.speak("Decreasing Volume")

                self.system.decrease_volume()

            elif action == "mute":

                self.update("Muting Volume")

                self.speaker.speak("Muting Volume")

                self.system.mute()

            return

        # ===============================================
        # KEYBOARD
        # ===============================================

        elif intent == "KEYBOARD":

            action = data["action"]

            if action == "copy":

                self.update("Copy")

                self.keyboard.copy()

            elif action == "paste":

                self.update("Paste")

                self.keyboard.paste()

            elif action == "cut":

                self.update("Cut")

                self.keyboard.cut()

            elif action == "undo":

                self.update("Undo")

                self.keyboard.undo()

            elif action == "redo":

                self.update("Redo")

                self.keyboard.hotkey("ctrl", "y")

            elif action == "select_all":

                self.update("Select All")

                self.keyboard.select_all()

            elif action == "press":

                key = data["target"]

                self.update(f"Pressing {key}")

                self.speaker.speak(f"Pressing {key}")

                self.keyboard.press_key(key)

            return

        # ===============================================
        # TYPE
        # ===============================================

        elif intent == "TYPE":

            text = data["text"]

            if text:

                self.update(f"Typing : {text}")

                self.speaker.speak("Typing")

                self.keyboard.type_text(text)

            return

        # ===============================================
        # MOUSE
        # ===============================================

        elif intent == "MOUSE":

            action = data["action"]

            if action == "click":

                self.mouse.click()

            elif action == "double":

                self.mouse.double_click()

            elif action == "right":

                self.mouse.right_click()

            elif action == "scroll_up":

                self.mouse.scroll_up()

            elif action == "scroll_down":

                self.mouse.scroll_down()

            return

        # ===============================================
        # SCREENSHOT
        # ===============================================

        elif intent == "SCREENSHOT":

            self.update("Taking Screenshot")

            self.speaker.speak("Taking Screenshot")

            self.system.screenshot()

            return

        # ===============================================
        # LOCK SCREEN
        # ===============================================

        elif intent == "LOCK":

            self.update("Locking Screen")

            self.speaker.speak("Locking Screen")

            self.system.lock()

            return

        # ===============================================
        # UNKNOWN
        # ===============================================

        else:

            self.update("Unknown Command")

            self.speaker.speak("Sorry, I did not understand.")

    # ==================================================
    # START ASSISTANT
    # ==================================================

    def start(self):

        self.speaker.speak("VoicePilot Started")

        while True:

            self.update("Listening...")

            command = self.listener.listen()

            if command is None:

                continue

            command = command.strip()

            if command == "":

                continue

            if command.lower() in [

                "exit",
                "quit",
                "stop assistant"

            ]:

                self.speaker.speak("Goodbye")

                break

            self.execute(command)