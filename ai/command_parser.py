"""
command_parser.py

Converts voice commands into structured data.
"""

from ai.intent_detector import IntentDetector


class CommandParser:

    def __init__(self):
        self.detector = IntentDetector()

    def parse(self, command: str):

        command = command.lower().strip().replace(".", "").replace(",", "")

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
                if word in command:
                    data["target"] = command.split(word, 1)[1].strip()
                    break

        # ==================================================
        # CLOSE APPLICATION
        # ==================================================
        elif intent == "CLOSE_APP":
            words = ["close", "exit", "quit"]
            for word in words:
                if word in command:
                    target_app = command.split(word, 1)[1].strip()
                    data["target"] = target_app if target_app else "active window"
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
        # KEYBOARD
        # ==================================================
        elif intent == "KEYBOARD":
            # 1. Define the key_map dictionary clearly so it can be read safely
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
                "scroll lock": "scrolllock",
                "insert": "insert"
            }

            # 2. Match macro actions
            if "copy" in command or "copy text" in command:
                data["action"] = "copy"

            elif "paste" in command or "paste text" in command:
                data["action"] = "paste"

            elif "cut" in command or "cut text" in command:
                data["action"] = "cut"

            elif "undo" in command or "undo text" in command:
                data["action"] = "undo"

            elif "redo" in command or "redo text" in command:
                data["action"] = "redo"

            elif "select all" in command or "select" in command or "select text" in command:
                data["action"] = "select_all"

            # 3. Fallback to basic button presses
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

        return data


if __name__ == "__main__":
    parser = CommandParser()
    while True:
        cmd = input("Command : ")
        if cmd.lower() == "exit":
            break
        print(parser.parse(cmd))