"""
intent_detector.py

Detects the user's intent from a voice command.
"""

from typing import Optional


class IntentDetector:

    def __init__(self):
        self.intent_keywords = {
            "OPEN_APP": [
                "open",
                "launch",
                "start",
                "run"
            ],

            "CLOSE_APP": [
                "close",
                "exit",
                "quit",
                "terminate"
            ],

            "SEARCH_WEB": [
                "search",
                "google",
                "find",
                "look up"
            ],

            "OPEN_FOLDER": [
                "folder",
                "directory",
                "drive"
            ],

            "SYSTEM_CONTROL": [
                "volume",
                "brightness",
                "shutdown",
                "restart",
                "lock",
                "sleep",
                "screenshot"
            ],

            "KEYBOARD": [
                "type",
                "press",
                "copy",
                "paste",
                "delete"
            ],

            "MOUSE": [
                "click",
                "double click",
                "right click",
                "scroll",
                "move cursor"
            ]
        }

    def detect_intent(self, command: str) -> Optional[str]:

        command = command.lower()

        for intent, keywords in self.intent_keywords.items():

            for keyword in keywords:

                if keyword in command:
                    return intent

        return "UNKNOWN"