import speech_recognition as sr


class SpeechToText:
    """
    Handles microphone input and converts speech to text.
    """

    def __init__(self):
        self.recognizer = sr.Recognizer()

        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8

    def listen(self):
        """
        Listen once and return recognized text.
        """

        with sr.Microphone() as source:

            print("\n🎤 Listening...")

            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)

            print(f"You said: {text}")

            return text.lower()

        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""

        except sr.RequestError:
            print("Speech Recognition service unavailable.")
            return ""

        except Exception as e:
            print(e)
            return ""


if __name__ == "__main__":

    stt = SpeechToText()

    while True:

        command = stt.listen()

        if command:

            print(command)