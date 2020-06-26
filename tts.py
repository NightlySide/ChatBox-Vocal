import os

from gtts import gTTS
from playsound import playsound
from uuid import uuid4


def speak(texte):
    filename = str(uuid4()) + ".mp3"
    myobj = gTTS(text=texte, lang="fr", slow=False)
    myobj.save(filename)
    playsound(filename)
    os.unlink(filename)


if __name__ == "__main__":
    speak("Bonjour tout le monde !")
