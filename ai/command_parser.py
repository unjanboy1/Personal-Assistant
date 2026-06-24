"""
command_parser.py

Extracts useful information from a voice command.
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

        intent = self.detector.detect_intent(command)

        data = {
            "intent": intent,
            "command": command,
            "target": None,
            "query": None
        }

        # -------------------------
        # Open application
        # -------------------------
        if intent == "OPEN_APP":

            words = command.split()

            if "open" in words:
                idx = words.index("open")

                if idx + 1 < len(words):
                    data["target"] = " ".join(words[idx + 1:])

        # -------------------------
        # Search Google
        # -------------------------
        elif intent == "SEARCH_WEB":

            if "search" in command:

                query = command.replace("search", "")
                query = query.replace("google", "")
                query = query.strip()

                data["query"] = query

        # -------------------------
        # Open Folder
        # -------------------------
        elif intent == "OPEN_FOLDER":

            data["target"] = command

        return data


if __name__ == "__main__":

    parser = CommandParser()

    while True:

        cmd = input("Command : ")

        result = parser.parse(cmd)

        print(result)