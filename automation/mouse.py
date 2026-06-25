"""
mouse.py

Mouse automation for VoicePilot.
"""

import pyautogui

class MouseController:

    def click(self):
        pyautogui.click()
        print("Mouse Clicked")

    def double_click(self):
        pyautogui.doubleClick()
        print("Mouse Double Clicked")

    def right_click(self):
        pyautogui.rightClick()
        print("Mouse Right Clicked")

    def scroll_up(self):
        # A positive integer scrolls UP on Windows platforms
        pyautogui.scroll(1000)
        print("Scrolled Up")

    def scroll_down(self):
        # A negative integer scrolls DOWN on Windows platforms
        pyautogui.scroll(-1000)
        print("Scrolled Down")


if __name__ == "__main__":
    mouse = MouseController()

    while True:
        print("\n====== Mouse Menu ======")
        print("1. Click")
        print("2. Double Click")
        print("3. Right Click")
        print("4. Scroll Up")
        print("5. Scroll Down")
        print("6. Exit")

        choice = input("> ")

        if choice == "1":
            mouse.click()
        elif choice == "2":
            mouse.double_click()
        elif choice == "3":
            mouse.right_click()
        elif choice == "4":
            mouse.scroll_up()
        elif choice == "5":
            mouse.scroll_down()
        elif choice == "6":
            break