"""
text_to_speech.py

Handles robust text-to-speech functionality for VoicePilot.
"""

import pyttsx3


class TextToSpeech:

    def __init__(self):
        # Configuration parameters saved for clean runtime recreation
        self.rate = 175
        self.volume = 1.0

    def speak(self, text: str):
        """
        Speak the given text reliably using an isolated execution context instance.
        """
        if not text:
            return

        print(f"VoicePilot: {text}")

        try:
            # Reinitialization on-demand stops loop-deadlocks with speech_to_text threads
            engine = pyttsx3.init()
            engine.setProperty("rate", self.rate)
            engine.setProperty("volume", self.volume)

            voices = engine.getProperty("voices")
            if len(voices) > 1:
                engine.setProperty("voice", voices[1].id)
            else:
                engine.setProperty("voice", voices[0].id)

            engine.say(text)
            engine.runAndWait()
            # Cleanly unroll the driver resources
            engine.stop()
            del engine
        except Exception as e:
            print(f"[TTS Error Override]: {e}")

    def stop(self):
        pass


if __name__ == "__main__":
    speaker = TextToSpeech()
    speaker.speak("Hello. I am VoicePilot. Your intelligent desktop assistant.")