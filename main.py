import time
import speech_recognition as sr

from vocal_recognition import SpeechRecognition
from tts import speak
from dialogflow_handler import query_response


def talkback(recognizer, audio):
    print("-------------------------")
    try:
        texte = recognizer.recognize_google(audio , language="fr-FR")
        print("Vous avez dit : " + texte)
        speak(query_response(texte))
    except sr.UnknownValueError:
        print("L'audio n'a pas pu être compris")
    except sr.RequestError as e:
        print(f"Impossible d'envoyer la requête. Erreur : {e}")


if __name__ == "__main__":
    speech_reco = SpeechRecognition()
    speech_reco.start_listening(callback=talkback)
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        speech_reco.stop_listening()