import pyttsx3


class TextToSpeech:
    """
    Handles text-to-speech functionality for VoicePilot.
    """

    def __init__(self):

        self.engine = pyttsx3.init()

        # Speech Properties
        self.engine.setProperty("rate", 175)
        self.engine.setProperty("volume", 1.0)

        voices = self.engine.getProperty("voices")

        # Select female voice if available
        if len(voices) > 1:
            self.engine.setProperty("voice", voices[1].id)
        else:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text: str):
        """
        Speak the given text.
        """

        if not text:
            return

        print(f"VoicePilot: {text}")

        self.engine.say(text)
        self.engine.runAndWait()

    def stop(self):
        """
        Stop current speech.
        """
        self.engine.stop()


if __name__ == "__main__":

    speaker = TextToSpeech()

    speaker.speak(
        "Hello. I am VoicePilot. Your intelligent desktop assistant."
    )