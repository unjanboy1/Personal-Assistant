# 🎙️ VoicePilot – AI Desktop Voice Assistant

VoicePilot is a lightweight, Python-based desktop voice assistant designed to streamline Windows system operations through natural language commands. By integrating real-time speech recognition, text-to-speech feedback, and low-level system automation, VoicePilot provides a seamless, hands-free interface for everyday desktop workflows.

---

## 🔑 Key Features

* **🎤 Voice Recognition & Feedback:** Real-time speech-to-text processing paired with customizable text-to-speech audio responses and a continuous listening loop.
* **💻 Application Management:** Launch and close native Windows tools and third-party software (e.g., *Google Chrome*, *Notepad*, *Calculator*, *VS Code*).
* **📁 Directory & File Navigation:** Instant voice access to drives, system folders, and File Explorer locations (e.g., *Downloads*, *Documents*, *This PC*, *D: Drive*).
* **🌐 Web & Browser Automation:** Execute direct web searches via default browsers and launch target URL destinations like *GitHub* or *YouTube*.
* **⌨️ Keyboard & Input Automation:** Trigger multi-key shortcuts, standard keys (`Enter`, `Tab`, `Caps Lock`, etc.), and direct voice-to-text string typing.
* **🖱️ Precision Mouse Control:** Programmatic execution of left clicks, right clicks, double clicks, and directional scrolling.
* **⚙️ Hardware & Display Controls:** Dynamically adjust display brightness, system volume levels, audio mute states, and active camera hardware.
* **🔒 Windows System Operations:** Instant administrative controls for locking, sleeping, restarting, or shutting down the operating system, plus rapid screen capture.

---

## 🛠️ Built With

* **Core Runtime:** Python
* **Audio & Speech:** SpeechRecognition, Pyttsx3
* **System & Input Automation:** PyAutoGUI, Psutil, Screen Brightness Control
* **Vision & Media:** OpenCV
* **GUI & Web Services:** Tkinter, Webbrowser, Subprocess

---

## 🚀 Voice Command Reference

| Category | Example Voice Commands |
| :--- | :--- |
| **Applications** | `"Open Chrome"`, `"Open VS Code"`, `"Close Notepad"` |
| **Browser** | `"Search Machine Learning"`, `"Open YouTube"`, `"Open GitHub"` |
| **System Directories** | `"Open Downloads Folder"`, `"Open D Drive"`, `"Open This PC"` |
| **Keyboard Input** | `"Copy"`, `"Paste"`, `"Press Enter"`, `"Type Project Status"` |
| **Mouse Operations** | `"Left Click"`, `"Right Click"`, `"Double Click"`, `"Scroll Down"` |
| **Hardware & Display** | `"Increase Brightness"`, `"Mute Volume"`, `"Take Screenshot"`, `"Open Camera"` |
| **System Operations** | `"Lock Screen"`, `"Sleep Computer"`, `"Restart Computer"` |

---

## 🔮 Project Roadmap

Planned implementations for future releases:

* **Dynamic Software Discovery:** Automatic discovery and launch capabilities for any installed application or local directory file by name.
* **Conversational AI & LLM Integration:** Offline AI interaction mode alongside cloud-based API integrations (e.g., ChatGPT) for contextual reasoning.
* **Productivity Tools:** Voice-triggered alarms, reminders, calendar sync, OCR text extraction, email automation, and WhatsApp messaging.
* **Security & Authentication:** Multi-factor local access featuring biometrics (Face Recognition) and Voice-Print Authentication.

---

## 👥 Contributors

* **Maryam Amir**
* **Zaib**

---

## 📄 License

This project is developed for educational and research purposes.