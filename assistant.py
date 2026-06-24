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
        # Hardware interfaces
        self.listener = SpeechToText()
        self.speaker = TextToSpeech()

        # NLP Command Parser
        self.parser = CommandParser()

        # Automation Subsystems
        self.apps = AppController()
        self.browser = BrowserController()
        self.explorer = ExplorerController()
        self.keyboard = KeyboardController()
        self.mouse = MouseController()
        self.system = SystemController()

        # GUI callback hook
        self.callback = callback

    # -------------------------------------------------------------------------
    def update(self, message):
        """Prints to terminal and updates the Tkinter UI logs."""
        print(message)
        if self.callback:
            self.callback(message)

    # -------------------------------------------------------------------------
    def execute(self, command):
        """Processes the command, checks the intent, and triggers automation."""
        # Clean up input string
        command_clean = command.lower().strip()
        
        # 0. Quick Global Overrides (Optional bypass for simple logic)
        if command_clean in ["hello", "hi", "hey"]:
            self.update("Hello! How can I help you today?")
            self.speaker.speak("Hello! How can I help you today?")
            return

        # Fetch intent data from our Command Parser
        data = self.parser.parse(command)
        intent = data.get("intent")

        self.update(f"Command : {command}")

        # 1. APPLICATION AUTOMATION
        if intent == "OPEN_APP":
            target = data.get("target")
            if target:
                self.update(f"Opening {target}...")
                self.speaker.speak(f"Opening {target}")
                self.apps.open_app(target)

        elif intent == "CLOSE_APP":
            target = data.get("target")
            if target:
                self.update(f"Closing {target}...")
                self.speaker.speak(f"Closing {target}")
                # Make sure your AppController has a close_app method!
                self.apps.close_app(target)

        # 2. BROWSER AUTOMATION
        elif intent == "SEARCH_WEB":
            query = data.get("query")
            if query:
                self.update(f"Searching Google for: {query}")
                self.speaker.speak(f"Searching {query}")
                self.browser.search_google(query)

        # 3. FILE EXPLORER AUTOMATION
        elif intent == "OPEN_FOLDER":
            path = data.get("path")
            if path:
                self.update(f"Opening directory: {path}")
                self.explorer.open_folder(path)

        # 4. OS / HARDWARE SYSTEM CONTROLS
        elif intent == "VOLUME_UP":
            self.update("Increasing volume.")
            self.system.increase_volume()

        elif intent == "VOLUME_DOWN":
            self.update("Decreasing volume.")
            self.system.decrease_volume()

        elif intent == "MUTE_SYSTEM":
            self.update("Toggling system mute.")
            self.system.mute()

        elif intent == "SYSTEM_SHUTDOWN":
            self.update("Initiating system shutdown.")
            self.speaker.speak("Shutting down the system. Goodbye.")
            self.system.shutdown()

        # 5. KEYBOARD / MOUSE AUTOMATION (MACROS)
        elif intent == "PRESS_KEY":
            key = data.get("key")
            if key:
                self.keyboard.press(key)

        elif intent == "CLICK_MOUSE":
            x, y = data.get("x"), data.get("y")
            if x is not None and y is not None:
                self.mouse.click(x, y)

        # 6. STANDALONE CHAT INTENTS
        elif intent == "GREETING":
            reply = "Hello! I am ready to assist you."
            self.update(reply)
            self.speaker.speak(reply)

        # FALLBACK ENGINE
        else:
            self.update("Unknown Command")
            self.speaker.speak("Sorry, I did not understand.")

    # -------------------------------------------------------------------------
    def start(self):
        """Starts the core listener loop (Runs inside a background worker thread)."""
        self.speaker.speak("VoicePilot Started")

        while True:
            self.update("Listening...")
            command = self.listener.listen()

            # Ignore empty strings (e.g., ambient room noise clicks)
            if not command or command.strip() == "":
                continue

            # Check core system breakdown hooks
            if command.lower().strip() in ["exit", "quit", "stop", "shut down"]:
                self.update("Terminating VoicePilot session...")
                self.speaker.speak("Goodbye")
                break

            # Execute valid verbal payloads
            self.execute(command)