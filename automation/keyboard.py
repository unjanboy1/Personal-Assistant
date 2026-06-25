"""
keyboard.py

High-Speed Keyboard automation for VoicePilot.
"""

import pyautogui
import time
import pyperclip  # Built-in or easily installed via pip for instant typing

# Keep this minimal so everything runs at full speed
pyautogui.PAUSE = 0.01  


class KeyboardController:

    def type_text(self, text):
        # Give a split second for the window to settle, but use clipboard for instant printing
        time.sleep(0.2)
        
        # Save old clipboard contents safely
        old_clipboard = pyperclip.paste()
        
        # Copy new text to clipboard and instantly drop it into the window via Ctrl+V
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        
        # Restore old clipboard
        pyperclip.copy(old_clipboard)
        print(f"Instantly Typed: {text}")

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
    # ... (rest of your testing block stays identical)