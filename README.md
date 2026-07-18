# 🎙️ VoicePilot: AI-Powered Desktop Voice Assistant

VoicePilot is an advanced, Python-based desktop voice assistant engineered to enable seamless, hands-free control of the Windows operating system. By integrating real-time speech recognition, natural text-to-speech feedback, and robust GUI automation, VoicePilot translates natural language commands into instantaneous system actions.

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

* **Core Engine:** Python
* **Speech Processing:** SpeechRecognition (Audio parsing), pyttsx3 (Offline Text-to-Speech)
* **OS & Process Automation:** PyAutoGUI (Input emulation), psutil (Process tracking), subprocess (System calls)
* **Computer Vision:** OpenCV (Camera feed handling)
* **Hardware Utilities:** screen-brightness-control (Display manipulation)
* **GUI & Web:** Tkinter (Interface design), webbrowser (Web automation)

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

## ⚙️ Installation & Requirements

### Prerequisites
* Windows OS
* Python 3.8 or higher

### Setup Instruction
1. Clone the repository to your local machine.
2. Install the required dependencies using pip:
   ```bash
   pip install SpeechRecognition pyttsx3 pyautogui psutil screen-brightness-control opencv-python