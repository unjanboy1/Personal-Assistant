"""
intent_detector.py

Detects the user's intent from a voice command.
"""


class IntentDetector:

    def detect(self, command: str):

        command = command.lower().strip()

        # ==========================================
        # OPEN APPLICATION
        # ==========================================

        if command.startswith(("open ", "launch ", "start ")):

            if "drive" not in command \
            and "folder" not in command \
            and "camera" not in command:

                return "OPEN_APP"

        # ==========================================
        # CLOSE APPLICATION
        # ==========================================

        if command.startswith(("close ", "exit ", "quit ")):

            if "camera" not in command:

                return "CLOSE_APP"

        # ==========================================
        # GOOGLE SEARCH
        # ==========================================

        if "search" in command or "google" in command:

            return "SEARCH_WEB"

        # ==========================================
        # DRIVE
        # ==========================================

        if "drive" in command:

            return "OPEN_DRIVE"

        # ==========================================
        # FOLDER
        # ==========================================

        if "folder" in command:

            return "OPEN_FOLDER"

        # ==========================================
        # CAMERA
        # ==========================================

        if "open camera" in command \
        or "start camera" in command \
        or "launch camera" in command:

            return "OPEN_CAMERA"

        if "close camera" in command:

            return "CLOSE_CAMERA"

        # ==========================================
        # BRIGHTNESS
        # ==========================================

        if "brightness" in command:

            return "BRIGHTNESS"

        # ==========================================
        # VOLUME
        # ==========================================

        if "volume" in command:

            return "VOLUME"

        # ==========================================
        # SCREENSHOT
        # ==========================================

        if "screenshot" in command:

            return "SCREENSHOT"

        # ==========================================
        # LOCK SCREEN
        # ==========================================

        if command in [
            "lock screen",
            "lock my screen",
            "lock computer",
            "lock pc"
        ]:

            return "LOCK"

        # ==========================================
        # TYPE
        # ==========================================

        if command.startswith("type ") \
        or command.startswith("write "):

            return "TYPE"

        # ==========================================
        # KEYBOARD COMMANDS
        # ==========================================

        keyboard_words = [

            "copy",
            "paste",
            "cut",
            "undo",
            "redo",
            "select all",

            "enter",
            "tab",
            "backspace",
            "delete",
            "space",

            "escape",
            "esc",

            "home",
            "end",

            "page up",
            "page down",

            "up",
            "down",
            "left",
            "right",

            "caps lock",
            "capslock",

            "num lock",
            "scroll lock",

            "insert"

        ]

        if command.startswith("press "):

            return "KEYBOARD"

        if command in keyboard_words:

            return "KEYBOARD"

        if any(command.startswith(word) for word in keyboard_words):

            return "KEYBOARD"

        # ==========================================
        # MOUSE
        # ==========================================

        mouse_commands = [

            "click",
            "double click",
            "right click",
            "left click",
            "scroll up",
            "scroll down"

        ]

        if command in mouse_commands:

            return "MOUSE"

        # ==========================================
        # UNKNOWN
        # ==========================================

        return "UNKNOWN"


if __name__ == "__main__":

    detector = IntentDetector()

    while True:

        cmd = input("Command : ")

        print(detector.detect(cmd))