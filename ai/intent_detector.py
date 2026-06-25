"""
intent_detector.py

Smart intent detector for VoicePilot.
"""


class IntentDetector:

    def detect(self, command: str):

        command = command.lower().strip()

        # -------------------------
        # Applications
        # -------------------------

        if command.startswith(("open ", "launch ", "start ")):

            return "OPEN_APP"

        # -------------------------
        # Browser
        # -------------------------

        if "search" in command or "google" in command:

            return "SEARCH_WEB"

        # -------------------------
        # Explorer
        # -------------------------

        if "drive" in command:

            return "OPEN_DRIVE"

        if "folder" in command:

            return "OPEN_FOLDER"

        # -------------------------
        # Brightness
        # -------------------------

        if "brightness" in command:

            return "BRIGHTNESS"

        # -------------------------
        # Volume
        # -------------------------

        if "volume" in command:

            return "VOLUME"

        # -------------------------
        # Screenshot
        # -------------------------

        if "screenshot" in command:

            return "SCREENSHOT"

        # -------------------------
        # Lock
        # -------------------------

        if "lock" in command:

            return "LOCK"

        # -------------------------
        # Mouse
        # -------------------------

        if "click" in command:

            return "MOUSE"

        # -------------------------
        # Keyboard
        # -------------------------

        if command.startswith("type"):

            return "TYPE"

        return "UNKNOWN"