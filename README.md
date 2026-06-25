
# 🎙️ VoicePilot – AI Desktop Voice Assistant

VoicePilot is a Python-based desktop voice assistant that enables users to control their Windows computer using natural voice commands. It combines speech recognition, text-to-speech, and desktop automation to perform everyday tasks hands-free.

The assistant can launch applications, search the web, control system settings, automate keyboard and mouse actions, and interact with Windows through simple voice commands.
---

# Features

## 🎤 Voice Recognition
- Real-time voice command recognition
- Speech-to-text conversion
- Text-to-speech responses
- Continuous listening mode

---

## 💻 Application Control
- Open desktop applications
- Close running applications
- Launch Windows built-in programs
- Open installed software

Example Commands:
- Open Chrome
- Open Notepad
- Open Calculator
- Close Chrome
- Close Notepad

---

## 📁 File & Folder Management
- Open folders
- Open drives
- Open File Explorer
- Navigate through Windows directories

Example Commands:
- Open D Drive
- Open Downloads Folder
- Open Documents
- Open This PC

---

## 🌐 Browser Automation
- Open websites
- Search Google
- Launch browser automatically

Example Commands:
- Search Python tutorials
- Search AI Projects
- Open YouTube
- Open GitHub

---

## ⌨ Keyboard Automation
Supports keyboard shortcuts and key presses.

Commands include:

- Copy
- Paste
- Cut
- Undo
- Redo
- Select All
- Press Enter
- Press Tab
- Press Escape
- Press Backspace
- Press Delete
- Press Space
- Press Home
- Press End
- Press Page Up
- Press Page Down
- Press Caps Lock
- Press Num Lock
- Press Scroll Lock

Typing Commands:

- Type Hello World
- Type My Name is Maryam

---

## 🖱 Mouse Automation

Supports:

- Left Click
- Right Click
- Double Click
- Scroll Up
- Scroll Down

---

## 💡 Brightness Control

Control screen brightness through voice.

Commands:

- Increase Brightness
- Decrease Brightness
- Maximum Brightness
- Minimum Brightness

---

## 🔊 Volume Control

Supports:

- Increase Volume
- Decrease Volume
- Mute Volume
- Unmute Volume

---

## 📸 Screenshot

Take screenshots instantly.

Command:

- Take Screenshot

---

## 📷 Camera Control

Supports opening and closing the Windows Camera.

Commands:

- Open Camera
- Close Camera

---

## 🔒 System Controls

Supports:

- Lock Screen
- Restart Computer
- Shutdown Computer
- Sleep Computer

---

# Upcoming Features

The following features are planned for future versions:

- Smart application finder
- Open any installed software automatically
- Open any file by voice
- Open any folder by name
- AI conversation mode
- Weather information
- Time and date queries
- Calculator
- Music player controls
- Email automation
- WhatsApp automation
- OCR (Text extraction from images)
- Face recognition login
- Voice authentication
- Multiple language support
- ChatGPT integration
- Offline AI mode
- Smart reminders
- Alarm system
- Calendar integration

---

# Technologies Used

- Python
- SpeechRecognition
- Pyttsx3
- PyAutoGUI
- OpenCV
- Psutil
- Screen Brightness Control
- Tkinter
- Webbrowser
- Subprocess

---

# Project Structure

```
VoicePilot/
│
├── app.py
├── assistant.py
├── README.md
├── requirements.txt
│
├── speech/
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│
├── ai/
│   ├── intent_detector.py
│   └── command_parser.py
│
├── automation/
│   ├── apps.py
│   ├── browser.py
│   ├── explorer.py
│   ├── keyboard.py
│   ├── mouse.py
│   └── system.py
│
├── ui/
│   ├── main_window.py
│   └── widgets.py
│
├── utils/
│   ├── config.py
│   └── helpers.py
│
└── assets/
```

---

# Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project

```bash
cd VoicePilot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python app.py
```

---

# Example Voice Commands

### Applications

- Open Chrome
- Open Notepad
- Open VS Code
- Close Chrome

### Browser

- Search Python Programming
- Search Machine Learning
- Open YouTube

### Keyboard

- Copy
- Paste
- Undo
- Select All
- Press Enter
- Press Backspace
- Press Caps Lock

### Mouse

- Click
- Right Click
- Double Click
- Scroll Down

### System

- Increase Brightness
- Decrease Brightness
- Increase Volume
- Take Screenshot
- Open Camera
- Lock Screen

---




