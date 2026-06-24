"""
helpers.py

Reusable helper functions.
"""

import datetime
import os


def clean_command(command: str) -> str:

    return command.lower().strip()


def current_time():

    return datetime.datetime.now().strftime("%I:%M %p")


def current_date():

    return datetime.datetime.now().strftime("%d-%m-%Y")


def timestamp():

    return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")


def file_exists(path):

    return os.path.exists(path)


def print_header(title):

    print("\n" + "=" * 50)

    print(title)

    print("=" * 50)