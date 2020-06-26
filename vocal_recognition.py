import time

import speech_recognition as sr


class SpeechRecognition:
    def __init__(self):
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        # On crée la fonction d'arrêt
        self._stop_listening = None

    def start_listening(self, callback=None):
        """ Permet de lancer l'écoute du micro en arrière-plan
        """
        # On ajuste au bruit ambiant
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

        if callback is None:
            callback = self._listening_callback
        self._stop_listening = self.r.listen_in_background(self.m, callback)
        print("Je vous écoute")

    def stop_listening(self):
        """ Permet d'arrêter l'écoute du micro en arrière-plan
        """
        self._stop_listening(wait_for_stop=False)
        print("Arrêt de l'écoute en arrière plan")

    @staticmethod
    def _listening_callback(recognizer, audio):
        """ Fonction appellée en arrière plan dans un thread à part
        """
        # On a récupéré des données on va essayer de le traduire
        try:
            print("Vous avez dit : " + recognizer.recognize_google(audio , language="fr-FR"))
        except sr.UnknownValueError:
            print("L'audio n'a pas pu être compris")
        except sr.RequestError as e:
            print(f"Impossible d'envoyer la requête. Erreur : {e}")


if __name__ == "__main__":
    speech_reco = SpeechRecognition()
    try:
        speech_reco.start_listening()
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        speech_reco.stop_listening()
        print("Arrêt de l'écoute")
