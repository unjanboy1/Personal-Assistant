"""
keyboard.py

High-Speed Keyboard automation for VoicePilot.
"""

import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.05  


class KeyboardController:

    def type_text(self, text):
        time.sleep(0.2)
        old_clipboard = pyperclip.paste()
        pyperclip.copy(text)
        pyautogui.hotkey("ctrl", "v")
        time.sleep(0.1)  # Gives OS time to release clipboard handle safely
        pyperclip.copy(old_clipboard)
        print(f"Instantly Typed: {text}")

    def press_key(self, key):
        pyautogui.press(key)
        print(f"Pressed: {key}")

    def hotkey(self, *keys):
        pyautogui.hotkey(*keys)
        print(f"Hotkey: {' + '.join(keys)}")

    def copy(self):
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "c")
        print("Triggered System Copy")

    def paste(self):
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "v")
        print("Triggered System Paste")

    def cut(self):
        time.sleep(0.1)
        pyautogui.hotkey("ctrl", "x")
        print("Triggered System Cut")

    def undo(self):
        pyautogui.hotkey("ctrl", "z")

    def select_all(self):
        pyautogui.hotkey("ctrl", "a")