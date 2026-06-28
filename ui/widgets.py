"""
VoicePilot UI Package
Contains:
- Main Window
- Widgets
"""
import tkinter as tk
from tkinter import scrolledtext

class StatusLabel(tk.Label):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, text="Ready", **kwargs)

class OutputBox(scrolledtext.ScrolledText):
    def __init__(self, parent, **kwargs):
        # A scrollable text box for the assistant's responses
        super().__init__(parent, wrap=tk.WORD, state=tk.DISABLED, **kwargs)
        
    def write(self, text):
        """Allows the assistant to log messages here using self.output.write(text)"""
        self.config(state=tk.NORMAL)   # Temporarily unlock the box to add text
        self.insert(tk.END, text + "\n") # Insert the text with a new line
        self.config(state=tk.DISABLED) # Lock it back up so the user can't edit it
        self.see(tk.END)               # Auto-scroll to the bottom