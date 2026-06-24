"""
explorer.py

Controls Windows File Explorer.
"""

import os
import subprocess


class ExplorerController:

    def open_this_pc(self):
        try:
            subprocess.Popen("explorer")
            print("Opened This PC.")
            return True
        except Exception as e:
            print(e)
            return False

    def open_drive(self, drive_letter):

        drive_letter = drive_letter.upper().replace(":", "")

        path = f"{drive_letter}:\\"

        if os.path.exists(path):
            subprocess.Popen(f'explorer "{path}"')
            print(f"Opened {path}")
            return True

        print("Drive not found.")
        return False

    def open_folder(self, folder_path):

        if os.path.exists(folder_path):
            subprocess.Popen(f'explorer "{folder_path}"')
            print("Folder opened.")
            return True

        print("Folder not found.")
        return False