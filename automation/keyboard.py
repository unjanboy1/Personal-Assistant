"""
keyboard.py

Keyboard automation for VoicePilot.
"""

import pyautogui


class KeyboardController:

    def type_text(self, text):

        pyautogui.write(text, interval=0.05)

        print(f"Typed: {text}")

    def press_key(self, key):

        pyautogui.press(key)

        print(f"Pressed: {key}")

    def hotkey(self, *keys):

        pyautogui.hotkey(*keys)

        print(f"Hotkey: {' + '.join(keys)}")

    def copy(self):

        pyautogui.hotkey("ctrl", "c")

    def paste(self):

        pyautogui.hotkey("ctrl", "v")

    def cut(self):

        pyautogui.hotkey("ctrl", "x")

    def undo(self):

        pyautogui.hotkey("ctrl", "z")

    def select_all(self):

        pyautogui.hotkey("ctrl", "a")


if __name__ == "__main__":

    keyboard = KeyboardController()

    while True:

        print("\n====== Keyboard Test ======")
        print("1. Type Text")
        print("2. Press Enter")
        print("3. Copy")
        print("4. Paste")
        print("5. Exit")

        choice = input("> ")

        if choice == "1":

            text = input("Text : ")

            keyboard.type_text(text)

        elif choice == "2":

            keyboard.press_key("enter")

        elif choice == "3":

            keyboard.copy()

        elif choice == "4":

            keyboard.paste()

        elif choice == "5":
            break