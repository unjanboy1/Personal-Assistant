"""
intent_detector.py

Detects the user's intent from a voice command.
"""


class IntentDetector:

    def detect(self, command: str):
        # Clean speech artifacts and common punctuation
        command = command.lower().strip().replace(".", "").replace(",", "")

        # Clean spaces between letters like "c u t"
        if "".join(command.split()) in ["cut", "copy", "paste", "undo", "redo"]:
            command = "".join(command.split())

        # ==========================================
        # OPEN APPLICATION
        # ==========================================
        if command.startswith(("open ", "launch ", "start ")):
            if "drive" not in command and "folder" not in command and "camera" not in command:
                return "OPEN_APP"

        # ==========================================
        # CLOSE APPLICATION
        # ==========================================
        if "close" in command or "exit" in command or "quit" in command:
            if "camera" not in command:
                return "CLOSE_APP"

        # ==========================================
        # GOOGLE SEARCH
        # ==========================================
        if "search" in command or "google" in command:
            return "SEARCH_WEB"

        # ==========================================
        # DRIVE / FOLDER / CAMERA
        # ==========================================
        if "drive" in command:
            return "OPEN_DRIVE"
        if "folder" in command:
            return "OPEN_FOLDER"
        if "open camera" in command or "start camera" in command or "launch camera" in command:
            return "OPEN_CAMERA"
        if "close camera" in command:
            return "CLOSE_CAMERA"

        # ==========================================
        # SYSTEM SETTINGS
        # ==========================================
        if "brightness" in command:
            return "BRIGHTNESS"
        if "volume" in command:
            return "VOLUME"
        if "screenshot" in command:
            return "SCREENSHOT"
        if any(w in command for w in ["lock screen", "lock my screen", "lock computer", "lock pc"]):
            return "LOCK"

        # ==========================================
        # TYPE
        # ==========================================
        if command.startswith("type ") or command.startswith("write "):
            return "TYPE"

        # ==========================================
        # MOUSE
        # ==========================================
        if any(m in command for m in ["click", "scroll"]):
            return "MOUSE"

        # ==========================================
        # KEYBOARD COMMANDS (Relaxed flexible checks)
        # ==========================================
        keyboard_shortcuts = ["copy", "paste", "cut", "undo", "redo", "select all", "select"]
        if any(shortcut in command for shortcut in keyboard_shortcuts):
            return "KEYBOARD"

        keyboard_keys = [
            "enter", "tab", "backspace", "delete", "space", "escape", "esc",
            "home", "end", "page up", "page down", "up", "down", "left", "right",
            "caps lock", "capslock", "num lock", "scroll lock", "insert"
        ]
        if command.startswith("press ") or any(key in command for key in keyboard_keys):
            return "KEYBOARD"

        return "UNKNOWN"