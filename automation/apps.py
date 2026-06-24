"""
apps.py

Handles opening and closing desktop applications.
"""

import subprocess
import os
import psutil


class AppController:

    def __init__(self):

        self.apps = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

            "notepad": "notepad.exe",

            "calculator": "calc.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe",

            "vscode": r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        }

    # --------------------------------------

    def open_app(self, app_name):

        app_name = app_name.lower()

        if app_name not in self.apps:
            return False

        try:

            subprocess.Popen(self.apps[app_name])

            print(f"{app_name} opened.")

            return True

        except Exception as e:

            print(e)

            return False

    # --------------------------------------

    def close_app(self, app_name):

        app_name = app_name.lower()

        processes = {

            "chrome": "chrome.exe",

            "notepad": "notepad.exe",

            "calculator": "CalculatorApp.exe",

            "paint": "mspaint.exe",

            "cmd": "cmd.exe",

            "explorer": "explorer.exe",

            "vscode": "Code.exe"
        }

        if app_name not in processes:
            return False

        target = processes[app_name]

        for proc in psutil.process_iter():

            try:

                if proc.name() == target:

                    proc.kill()

            except Exception:
                pass

        print(f"{app_name} closed.")

        return True


if __name__ == "__main__":

    app = AppController()

    while True:

        print()

        print("1. Open App")
        print("2. Close App")
        print("3. Exit")

        choice = input("> ")

        if choice == "1":

            name = input("App Name : ")

            app.open_app(name)

        elif choice == "2":

            name = input("App Name : ")

            app.close_app(name)

        else:
            break