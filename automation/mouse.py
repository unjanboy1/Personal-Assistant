"""
mouse.py

Mouse automation for VoicePilot.
"""

import pyautogui

# Adjust these settings globally to handle modern Windows UI environments smoothly
pyautogui.FAILSAFE = False  # Prevents crashing if mouse reaches corner boundaries
pyautogui.PAUSE = 0.1       # Slight delay to ensure the OS registers clicks correctly


class MouseController:

    def click(self):
        pyautogui.click()
        print("Left Click")

    def double_click(self):
        pyautogui.doubleClick()
        print("Double Click")

    def right_click(self):
        pyautogui.rightClick()
        print("Right Click")

    def move(self, x, y):
        pyautogui.moveTo(x, y, duration=0.4)
        print(f"Moved to ({x}, {y})")

    def scroll_up(self):
        pyautogui.scroll(500)
        print("Scrolled Up")

    def scroll_down(self):
        pyautogui.scroll(-500)
        print("Scrolled Down")

    def drag(self, x, y):
        pyautogui.dragTo(x, y, duration=0.5)


if __name__ == "__main__":
    mouse = MouseController()

    while True:
        print("\n====== Mouse Test ======")
        print("1. Click")
        print("2. Double Click")
        print("3. Right Click")
        print("4. Move")
        print("5. Scroll Up")
        print("6. Scroll Down")
        print("7. Exit")

        choice = input("> ")

        if choice == "1":
            mouse.click()
        elif choice == "2":
            mouse.double_click()
        elif choice == "3":
            mouse.right_click()
        elif choice == "4":
            x = int(input("X : "))
            y = int(input("Y : "))
            mouse.move(x, y)
        elif choice == "5":
            mouse.scroll_up()
        elif choice == "6":
            mouse.scroll_down()
        elif choice == "7":
            break