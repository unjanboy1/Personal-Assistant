"""
speech_to_text.py

Handles voice-to-text transformation with enhanced responsiveness for VoicePilot.
"""

import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        
        # Fixed sensitivity threshold keeps background noise from lowering mic accuracy
        self.recognizer.energy_threshold = 300  
        self.recognizer.dynamic_energy_threshold = False  
        
        # Shorter trailing silence window for snappy responses
        self.recognizer.pause_threshold = 0.5  

    def listen(self):
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            try:
                # Set a clear phrase limit to process commands instantly
                audio = self.recognizer.listen(source, timeout=None, phrase_time_limit=5)
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Could not understand audio.")
                return None
            except sr.RequestError:
                print("Speech service down.")
                return None


if __name__ == "__main__":
    listener = SpeechToText()
    while True:
        listener.listen()