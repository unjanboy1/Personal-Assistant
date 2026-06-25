"""
browser.py

Browser automation for VoicePilot.
"""

import webbrowser
from urllib.parse import quote


class BrowserController:

    def open_google(self):
        webbrowser.open("https://www.google.com")
        print("Google opened.")

    def open_website(self, url):
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        print(f"Opened {url}")

    def search_google(self, query):
        query_encoded = quote(query)
        url = f"https://www.google.com/search?q={query_encoded}"
        webbrowser.open(url)
        print(f"Searching: {query}")


if __name__ == "__main__":
    browser = BrowserController()

    while True:
        print("\n===== Browser Test =====")
        print("1. Open Google")
        print("2. Search Google")
        print("3. Open Website")
        print("4. Exit")

        choice = input("> ")

        if choice == "1":
            browser.open_google()
        elif choice == "2":
            query = input("Search : ")
            browser.search_google(query)
        elif choice == "3":
            site = input("Website : ")
            browser.open_website(site)
        elif choice == "4":
            break