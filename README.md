# 🎙️ VoicePilot: AI-Powered Desktop Voice Assistant

[![Python Version](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic_/_Educational-green.svg)](https://opensource.org/licenses/)
[![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)](https://www.microsoft.com/windows)

**VoicePilot** is an advanced, Python-based desktop voice assistant engineered to enable seamless, hands-free control of Windows operating systems. By integrating real-time speech recognition, natural text-to-speech feedback, and robust GUI automation, VoicePilot translates natural language commands into instantaneous system actions. 

---

## 🚀 Key Features

### 🎤 Intelligent Speech Engine
* **Real-Time Recognition:** Low-latency processing of voice inputs.
* **Bi-directional Feedback:** Clear, customizable text-to-speech verbal confirmations.
* **Continuous Listening:** Background execution waiting for your prompt.

### 💻 System & Application Control
* **Process Management:** Launch and terminate standard Windows applications or third-party software (e.g., Chrome, VS Code, Notepad).
* **Power & Security:** Voice-triggered commands to lock, sleep, restart, or safely shut down the system.
* **Hardware Integration:** Direct toggle control for the Windows Camera and instant screenshot capturing.

### 📂 File & Directory Navigation
* Native integration with Windows File Explorer.
* Direct vocal navigation to key system directories (e.g., Documents, Downloads, local drives).

### ⌨️ Hands-Free Hardware Automation
* **Keyboard Emulation:** Full support for system shortcuts, functional keypresses, and direct text dictation.
* **Mouse Emulation:** Trigger precise left, right, double clicks, and vertical scrolling on demand.
* **Peripherals Control:** Dynamic adjustment of screen brightness levels and system volume states.

---

## 🛠️ Tech Stack & Dependencies

VoicePilot leverages a robust suite of Python libraries to bridge speech processing with OS-level execution:

* **Core Engine:** `Python`
* **Speech Processing:** `SpeechRecognition` (Audio parsing), `pyttsx3` (Offline Text-to-Speech)
* **OS & Process Automation:** `PyAutoGUI` (Input emulation), `psutil` (Process tracking), `subprocess` (System calls)
* **Computer Vision:** `OpenCV` (Camera feed handling)
* **Hardware Utilities:** `screen-brightness-control` (Display manipulation)
* **GUI & Web:** `Tkinter` (Interface design), `webbrowser` (Web automation)

---

## 💬 Command Reference

| Category | Voice Command Examples | Action Performed |
| :--- | :--- | :--- |
| **Applications** | `"Open Chrome"`, `"Open Notepad"`, `"Close Chrome"` | Launches or terminates target processes. |
| **Browser** | `"Search Python tutorials"`, `"Open YouTube"`, `"Open GitHub"` | Performs web searches or navigates directly to URLs. |
| **File System** | `"Open Downloads Folder"`, `"Open D Drive"`, `"Open This PC"` | Spawns File Explorer at designated directories. |
| **Keyboard** | `"Copy"`, `"Paste"`, `"Select All"`, `"Press Enter"` | Simulates system-wide keyboard shortcuts/keys. |
| **Text Dictation**| `"Type Hello World"` | Injects simulated keystrokes at the cursor position. |
| **Mouse** | `"Click"`, `"Right Click"`, `"Scroll Down"` | Executes mouse actions at current coordinates. |
| **Hardware** | `"Increase Brightness"`, `"Mute Volume"`, `"Take Screenshot"`| Dynamically alters system states & captures screen. |
| **System** | `"Lock Screen"`, `"Sleep Computer"`, `"Open Camera"` | Changes power states or initiates utility features. |

---

## 🗺️ Roadmap & Future Vision

Our long-term objective is to transition VoicePilot from a utility assistant into a fully contextual, intelligent desktop companion. 

### Phase 1: Enhanced Automation & Utilities
* [ ] **Smart Application Finder:** Automatically scan and launch any installed software without hardcoded paths.
* [ ] **Advanced File Indexing:** Locate and open specific files/folders instantly by name.
* [ ] **Personal Productivity:** Voice-automated emails, WhatsApp messaging, and calendar integrations.
* [ ] **Media & Time:** Smart alarms, dynamic timers, and unified media player controls.

### Phase 2: AI & Security Integration
* [ ] **Large Language Model (LLM) Integration:** Support for ChatGPT/local offline AI models for conversational depth.
* [ ] **Computer Vision Capabilities:** OCR engine for on-screen text extraction and face recognition login.
* [ ] **Biometric Voice Verification:** Secure execution of administrative commands via voiceprint matching.
* [ ] **Localization:** Multilingual speech-to-text processing.

---

## 👥 Contributors

We appreciate the dedication and efforts of our development team:

* **Maryam Amir**
* **Zaib**

---

## 📄 License & Academic Note

This project is developed primarily for academic, educational, and research purposes. All rights reserved to the original authors.