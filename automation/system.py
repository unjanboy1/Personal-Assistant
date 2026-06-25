"""
system.py

System automation for VoicePilot.
"""

import os
import pyautogui
import screen_brightness_control as sbc


class SystemController:

    def shutdown(self):
        os.system("shutdown /s /t 1")

    def restart(self):
        os.system("shutdown /r /t 1")

    def lock(self):
        os.system("rundll32.exe user32.dll,LockWorkStation")

    def sleep(self):
        os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")

    # -------------------------
    # Screenshot
    # -------------------------

    def screenshot(self, filename="screenshot.png"):
        image = pyautogui.screenshot()
        image.save(filename)
        print(f"Screenshot saved as {filename}")

    # -------------------------
    # Brightness
    # -------------------------

    def increase_brightness(self):
        try:
            # Safely grab current primary display brightness level
            current_list = sbc.get_brightness()
            current = current_list[0] if current_list else 50
            sbc.set_brightness(min(current + 10, 100))
            print("Brightness Increased")
        except Exception as e:
            print(f"Brightness Error: {e}")

    def decrease_brightness(self):
        try:
            current_list = sbc.get_brightness()
            current = current_list[0] if current_list else 50
            sbc.set_brightness(max(current - 10, 0))
            print("Brightness Decreased")
        except Exception as e:
            print(f"Brightness Error: {e}")

    def set_brightness(self, value):
        try:
            value = max(0, min(100, value))
            sbc.set_brightness(value)
            print(f"Brightness set to {value}%")
        except Exception as e:
            print(f"Brightness Error: {e}")


if __name__ == "__main__":
    system = SystemController()

    while True:
        print("\n====== System Menu ======")
        print("1. Screenshot")
        print("2. Increase Brightness")
        print("3. Decrease Brightness")
        print("4. Set Brightness")
        print("5. Lock PC")
        print("6. Exit")

        choice = input("> ")

        if choice == "1":
            system.screenshot()
        elif choice == "2":
            system.increase_brightness()
        elif choice == "3":
            system.decrease_brightness()
        elif choice == "4":
            value = int(input("Brightness (0-100): "))
            system.set_brightness(value)
        elif choice == "5":
            system.lock()
        elif choice == "6":
            break