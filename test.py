from speech.speech_to_text import SpeechToText
from speech.text_to_speech import TextToSpeech

listener = SpeechToText()
speaker = TextToSpeech()

while True:

    command = listener.listen()

    if command:
        speaker.speak(f"You said {command}")

    if command == "exit":
        speaker.speak("Goodbye.")
        break