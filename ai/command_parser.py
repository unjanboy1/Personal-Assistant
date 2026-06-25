"""
command_parser.py

Converts voice commands into structured data.
"""

from ai.intent_detector import IntentDetector


class CommandParser:

    def __init__(self):
        self.detector = IntentDetector()

    def parse(self, command: str):

        command = command.lower().strip()

        intent = self.detector.detect(command)

        data = {
            "intent": intent,
            "target": None,
            "query": None,
            "action": None,
            "text": None
        }

        # ==================================================
        # OPEN APPLICATION
        # ==================================================

        if intent == "OPEN_APP":

            words = ["open", "launch", "start"]

            for word in words:

                if command.startswith(word):

                    app = command.replace(word, "", 1).strip()

                    data["target"] = app

                    break

        # ==================================================
        # CLOSE APPLICATION
        # ==================================================

        elif intent == "CLOSE_APP":

            words = ["close", "exit", "quit"]

            for word in words:

                if command.startswith(word):

                    app = command.replace(word, "", 1).strip()

                    data["target"] = app

                    break

        # ==================================================
        # GOOGLE SEARCH
        # ==================================================

        elif intent == "SEARCH_WEB":

            query = command

            for word in ["search", "google", "for"]:

                query = query.replace(word, "")

            data["query"] = query.strip()

        # ==================================================
        # OPEN DRIVE
        # ==================================================

        elif intent == "OPEN_DRIVE":

            if "c" in command:
                data["target"] = "C"

            elif "d" in command:
                data["target"] = "D"

            elif "e" in command:
                data["target"] = "E"

            elif "f" in command:
                data["target"] = "F"

        # ==================================================
        # OPEN FOLDER
        # ==================================================

        elif intent == "OPEN_FOLDER":

            folder = command

            folder = folder.replace("open", "")
            folder = folder.replace("folder", "")

            data["target"] = folder.strip()

        # ==================================================
        # CAMERA
        # ==================================================

        elif intent == "OPEN_CAMERA":

            data["action"] = "open"

        elif intent == "CLOSE_CAMERA":

            data["action"] = "close"

        # ==================================================
        # BRIGHTNESS
        # ==================================================

        elif intent == "BRIGHTNESS":

            if "increase" in command or "up" in command:

                data["action"] = "increase"

            elif "decrease" in command or "down" in command:

                data["action"] = "decrease"

            elif "maximum" in command or "max" in command:

                data["action"] = "maximum"

            elif "minimum" in command or "min" in command:

                data["action"] = "minimum"

        # ==================================================
        # VOLUME
        # ==================================================

        elif intent == "VOLUME":

            if "increase" in command or "up" in command:

                data["action"] = "increase"

            elif "decrease" in command or "down" in command:

                data["action"] = "decrease"

            elif "mute" in command:

                data["action"] = "mute"

            elif "unmute" in command:

                data["action"] = "unmute"
        # ==================================================
        # KEYBOARD
        # ==================================================

        elif intent == "KEYBOARD":

            key_map = {

                "enter": "enter",
                "return": "enter",

                "tab": "tab",

                "backspace": "backspace",

                "delete": "delete",

                "space": "space",

                "escape": "esc",
                "esc": "esc",

                "home": "home",
                "end": "end",

                "page up": "pageup",
                "page down": "pagedown",

                "up": "up",
                "down": "down",
                "left": "left",
                "right": "right",

                "caps lock": "capslock",
                "capslock": "capslock",

                "num lock": "numlock",
                "numlock": "numlock",

                "scroll lock": "scrolllock",
                "scrolllock": "scrolllock",

                "insert": "insert"
            }

            if "copy" in command:

                data["action"] = "copy"

            elif "paste" in command:

                data["action"] = "paste"

            elif "cut" in command:

                data["action"] = "cut"

            elif "undo" in command:

                data["action"] = "undo"

            elif "redo" in command:

                data["action"] = "redo"

            elif "select all" in command:

                data["action"] = "select_all"

            else:

                key = command

                if key.startswith("press "):
                    key = key.replace("press ", "", 1).strip()

                data["action"] = "press"
                data["target"] = key_map.get(key, key)

        # ==================================================
        # TYPE TEXT
        # ==================================================

        elif intent == "TYPE":

            text = command

            if text.startswith("type "):

                text = text.replace("type ", "", 1)

            elif text.startswith("write "):

                text = text.replace("write ", "", 1)

            data["text"] = text.strip()

        # ==================================================
        # MOUSE
        # ==================================================

        elif intent == "MOUSE":

            if "double" in command:

                data["action"] = "double"

            elif "right" in command:

                data["action"] = "right"

            elif "left" in command:

                data["action"] = "click"

            elif "scroll up" in command:

                data["action"] = "scroll_up"

            elif "scroll down" in command:

                data["action"] = "scroll_down"

            else:

                data["action"] = "click"

        # ==================================================
        # SCREENSHOT
        # ==================================================

        elif intent == "SCREENSHOT":

            data["action"] = "take"

        # ==================================================
        # LOCK SCREEN
        # ==================================================

        elif intent == "LOCK":

            data["action"] = "lock"

        # ==================================================
        # RETURN
        # ==================================================

        return data


if __name__ == "__main__":

    parser = CommandParser()

    while True:

        cmd = input("Command : ")

        if cmd.lower() == "exit":
            break

        print(parser.parse(cmd))