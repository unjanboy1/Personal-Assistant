"""
command_parser.py

Converts voice commands into structured actions.
"""

try:
    from ai.intent_detector import IntentDetector
except ModuleNotFoundError:
    from intent_detector import IntentDetector


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

        # =====================================================
        # OPEN APPLICATION
        # =====================================================

        if intent == "OPEN_APP":

            for word in ["open", "launch", "start"]:

                if command.startswith(word):

                    target = command.replace(word, "", 1).strip()

                    target = target.replace("application", "")
                    target = target.replace("app", "")

                    data["target"] = target.strip()

                    break

        # =====================================================
        # GOOGLE SEARCH
        # =====================================================

        elif intent == "SEARCH_WEB":

            query = command

            words = [
                "search",
                "google",
                "for",
                "search for"
            ]

            for w in words:
                query = query.replace(w, "")

            data["query"] = query.strip()

        # =====================================================
        # OPEN DRIVE
        # =====================================================

        elif intent == "OPEN_DRIVE":

            if "c drive" in command or "drive c" in command:
                data["target"] = "C"

            elif "d drive" in command or "drive d" in command:
                data["target"] = "D"

            elif "e drive" in command or "drive e" in command:
                data["target"] = "E"

            elif "f drive" in command or "drive f" in command:
                data["target"] = "F"

        # =====================================================
        # OPEN FOLDER
        # =====================================================

        elif intent == "OPEN_FOLDER":

            folder = command

            folder = folder.replace("open", "")
            folder = folder.replace("folder", "")

            data["target"] = folder.strip()

        # =====================================================
        # BRIGHTNESS
        # =====================================================

        elif intent == "BRIGHTNESS":

            if "increase" in command or "up" in command:

                data["action"] = "increase"

            elif "decrease" in command or "down" in command:

                data["action"] = "decrease"

            elif "maximum" in command or "max" in command:

                data["action"] = "maximum"

            elif "minimum" in command or "min" in command:

                data["action"] = "minimum"

        # =====================================================
        # VOLUME
        # =====================================================

        elif intent == "VOLUME":

            if "increase" in command or "up" in command:

                data["action"] = "increase"

            elif "decrease" in command or "down" in command:

                data["action"] = "decrease"

            elif "mute" in command:

                data["action"] = "mute"

        # =====================================================
        # SCREENSHOT
        # =====================================================

        elif intent == "SCREENSHOT":

            data["action"] = "take"

        # =====================================================
        # LOCK
        # =====================================================

        elif intent == "LOCK":

            data["action"] = "lock"

        # =====================================================
        # KEYBOARD COMMANDS
        # =====================================================

        elif "copy" == command:

            data["intent"] = "KEYBOARD"
            data["action"] = "copy"

        elif "paste" == command:

            data["intent"] = "KEYBOARD"
            data["action"] = "paste"

        elif "cut" == command:

            data["intent"] = "KEYBOARD"
            data["action"] = "cut"

        elif "undo" == command:

            data["intent"] = "KEYBOARD"
            data["action"] = "undo"

        elif "select all" in command:

            data["intent"] = "KEYBOARD"
            data["action"] = "select_all"

        elif command.startswith("press "):

            key = command.replace("press", "", 1).strip()

            data["intent"] = "KEYBOARD"
            data["action"] = "press"
            data["target"] = key

        elif command.startswith("type "):

            text = command.replace("type", "", 1).strip()

            data["intent"] = "TYPE"
            data["text"] = text

        # =====================================================
        # MOUSE
        # =====================================================

        elif "double click" in command:

            data["intent"] = "MOUSE"
            data["action"] = "double"

        elif "right click" in command:

            data["intent"] = "MOUSE"
            data["action"] = "right"

        elif "click" == command:

            data["intent"] = "MOUSE"
            data["action"] = "click"

        return data


if __name__ == "__main__":

    parser = CommandParser()

    while True:

        command = input("\nCommand : ")

        result = parser.parse(command)

        print(result)