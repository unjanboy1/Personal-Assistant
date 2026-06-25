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

        # -----------------------------------
        # Open Applications
        # -----------------------------------

        if intent == "OPEN_APP":

            for word in ["open", "launch", "start"]:

                if command.startswith(word):

                    data["target"] = command.replace(word, "", 1).strip()

                    break

        # -----------------------------------
        # Google Search
        # -----------------------------------

        elif intent == "SEARCH_WEB":

            query = command

            query = query.replace("search", "")
            query = query.replace("google", "")
            query = query.replace("for", "")

            data["query"] = query.strip()

        # -----------------------------------
        # Drive
        # -----------------------------------

        elif intent == "OPEN_DRIVE":

            if "c" in command:
                data["target"] = "C"

            elif "d" in command:
                data["target"] = "D"

            elif "e" in command:
                data["target"] = "E"

        # -----------------------------------
        # Brightness
        # -----------------------------------

        elif intent == "BRIGHTNESS":

            if "increase" in command or "up" in command:

                data["action"] = "increase"

            elif "decrease" in command or "down" in command:

                data["action"] = "decrease"

            elif "maximum" in command:

                data["action"] = "maximum"

            elif "minimum" in command:

                data["action"] = "minimum"

        # -----------------------------------
        # Volume
        # -----------------------------------

        elif intent == "VOLUME":

            if "increase" in command:

                data["action"] = "increase"

            elif "decrease" in command:

                data["action"] = "decrease"

            elif "mute" in command:

                data["action"] = "mute"

        # -----------------------------------
        # Screenshot
        # -----------------------------------

        elif intent == "SCREENSHOT":

            data["action"] = "take"

        # -----------------------------------
        # Lock
        # -----------------------------------

        elif intent == "LOCK":

            data["action"] = "lock"

        # -----------------------------------
        # Mouse
        # -----------------------------------

        elif intent == "MOUSE":

            if "double" in command:

                data["action"] = "double"

            elif "right" in command:

                data["action"] = "right"

            else:

                data["action"] = "click"

        # -----------------------------------
        # Keyboard
        # -----------------------------------

        elif intent == "TYPE":

            data["text"] = command.replace("type", "", 1).strip()

        return data


if __name__ == "__main__":

    parser = CommandParser()

    while True:

        command = input("Command : ")

        result = parser.parse(command)

        print(result)