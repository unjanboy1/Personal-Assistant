
# 🎙️ VoicePilot

VoicePilot is a Python-based desktop voice assistant designed to control Windows environments using natural language processing. By combining robust speech recognition, text-to-speech synthesis, and OS-level automation, VoicePilot delivers a hands-free desktop experience. 

Whether you need to launch applications, manipulate files, automate browser workflows, or control system hardware, VoicePilot executes your verbal commands in real time.

---

## 🚀 Key Features

* **Continuous Voice Recognition:** Real-time speech-to-text processing and text-to-speech confirmation.
* **Application & File Management:** Hands-free execution, termination, and directory navigation.
* **Peripherals Automation:** Full mouse navigation and keystroke macros via voice injection.
* **Hardware Control:** Granular adjustment of system audio, display brightness, and power states.

---

## 🛠️ Tech Stack & Dependencies

VoicePilot leverages a modular Python architecture utilizing the following core libraries:

* **Audio Pipeline:** `SpeechRecognition` (STT), `pyttsx3` (TTS)
* **OS Automation:** `pyautogui` (Input simulation), `subprocess`, `psutil` (Process management)
* **Hardware Interfacing:** `screen-brightness-control`
* **Computer Vision:** `opencv-python` (Camera & vision tasks)
* **GUI Engine:** `tkinter`
* **Networking:** `webbrowser`

---

## 📋 Supported Voice Commands

### 💻 System & Application Control
| Target | Sample Commands |
| :--- | :--- |
| **Applications** | `"Open Chrome"`, `"Open Notepad"`, `"Open Calculator"`, `"Close Chrome"` |
| **File System** | `"Open D Drive"`, `"Open Downloads Folder"`, `"Open Documents"`, `"Open This PC"` |
| **System States** | `"Lock Screen"`, `"Restart Computer"`, `"Shutdown Computer"`, `"Sleep Computer"` |
| **Hardware Perks**| `"Take Screenshot"`, `"Open Camera"`, `"Close Camera"` |

### 🌐 Web & Browser Automation
| Objective | Command Syntax |
| :--- | :--- |
| **Web Navigation** | `"Open YouTube"`, `"Open GitHub"` |
| **Search Queries** | `"Search Python tutorials"`, `"Search AI Projects"` |

### ⌨️ Input Automation (Mouse & Keyboard)
| Category | Supported Actions / Syntax |
| :--- | :--- |
| **Keyboard Modifiers** | `"Copy"`, `"Paste"`, `"Cut"`, `"Undo"`, `"Redo"`, `"Select All"` |
| **Standard Keys** | `"Press Enter"`, `"Press Tab"`, `"Press Escape"`, `"Press Backspace"`, `"Press Delete"` |
| **Navigation Keys** | `"Press Home"`, `"Press End"`, `"Press Page Up"`, `"Press Page Down"` |
| **Toggles** | `"Press Caps Lock"`, `"Press Num Lock"`, `"Press Scroll Lock"` |
| **Text Injection** | `"Type [Your Text Here]"` *(e.g., "Type Hello World")* |
| **Mouse Operations** | `"Left Click"`, `"Right Click"`, `"Double Click"`, `"Scroll Up"`, `"Scroll Down"` |

### 🎛️ Hardware Toggles
| Hardware | Commands |
| :--- | :--- |
| **Display Brightness** | `"Increase Brightness"`, `"Decrease Brightness"`, `"Maximum Brightness"`, `"Minimum Brightness"` |
| **System Audio** | `"Increase Volume"`, `"Decrease Volume"`, `"Mute Volume"`, `"Unmute Volume"` |

---

## 🛣️ Roadmap & Future Goals

The long-term objective of VoicePilot is to evolve from a command-matching engine into an intelligent, context-aware digital workplace assistant. Planned features include:

### 🧠 Intelligent Automation & AI
* Deep LLM/ChatGPT integration for conversational context.
* Offline AI execution mode for enhanced privacy.
* Smart application finder to dynamically locate non-pathed software binaries.
* OCR engine for image-to-text workflows.

### 🛡️ Security & Authentication
* Biometric security via face recognition login.
* Voice print authentication to restrict system access.

### 📅 Productivity Suite
* Natural language calendar, alarm, and reminder configuration.
* Automated messaging integrations (WhatsApp, Email clients).
* Live localized weather, date, and math computation parsing.
* Multi-language spoken dialect profiles.

---

## 👥 Contributors

* **Maryam Amir**
* **Zaib**

---

## 📄 License


This project is developed exclusively for educational and academic purposes.
