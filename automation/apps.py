"""
apps.py

Handles opening and closing desktop applications.
"""

import subprocess
import os
import psutil
import pyautogui


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
        """
        Universal closing function that handles apps, folders, and drives
        safely on both Windows 10 and Windows 11.
        """
        app_name = app_name.lower().strip()
        print(f"[Console Log]: Attempting to close: '{app_name}'")
        
        # 1. Direct Target: If you say close drive, folder, or active window
        if any(keyword in app_name for keyword in ["drive", "folder", "active window", "this window", "this"]):
            pyautogui.hotkey("alt", "f4")
            print("[Success]: Closed open drive/folder window via Alt+F4.")
            return

        # 2. Hardcoded App Name Mapping
        target_processes = []
        if app_name == "notepad":
            target_processes = ["notepad.exe", "windowsnotepad.exe"]
        elif app_name in ["chrome", "google chrome"]:
            target_processes = ["chrome.exe"]
        elif app_name in ["word", "ms word"]:
            target_processes = ["winword.exe"]
        elif app_name in ["excel", "ms excel"]:
            target_processes = ["excel.exe"]
        else:
            # Fallback for standard system application names
            target_processes = [app_name if app_name.endswith(".exe") else f"{app_name}.exe"]

        closed_any = False

        # 3. Terminate matching background processes
        for proc in psutil.process_iter():
            try:
                proc_name = proc.name().lower()
                if any(target in proc_name for target in target_processes):
                    proc.kill()
                    print(f"[Success]: Closed process: {proc.name()}")
                    closed_any = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # 4. Global Fallback
        if not closed_any:
            print(f"[Info]: No standalone background process matched. Using Alt+F4 fallback.")
            pyautogui.hotkey("alt", "f4")
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