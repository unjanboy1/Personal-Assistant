"""
explorer.py

Controls Windows File Explorer.
"""

import os
import subprocess


class ExplorerController:

    def open_this_pc(self):
        try:
            subprocess.Popen(["explorer"])
            print("Opened This PC.")
            return True
        except Exception as e:
            print(e)
            return False

    def open_drive(self, drive_letter):

        drive_letter = drive_letter.upper().replace(":", "").strip()

        path = f"{drive_letter}:\\"

        print("Trying to open:", path)

        if os.path.exists(path):

            subprocess.Popen(["explorer", path])

            print(f"Opened {path}")

            return True

        print("Drive not found.")

        return False

    def open_folder(self, folder_path):

        if os.path.exists(folder_path):

            subprocess.Popen(["explorer", folder_path])

            print("Folder opened.")

            return True

        print("Folder not found.")

        return False


if __name__ == "__main__":

    explorer = ExplorerController()

    while True:

        print("\n===== Explorer Test =====")
        print("1. Open This PC")
        print("2. Open Drive")
        print("3. Open Folder")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":

            explorer.open_this_pc()

        elif choice == "2":

            drive = input("Drive Letter: ")

            explorer.open_drive(drive)

        elif choice == "3":

            folder = input("Folder Path: ")

            explorer.open_folder(folder)

        elif choice == "4":

            break