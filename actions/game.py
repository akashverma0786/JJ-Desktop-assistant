import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        # pause to listen to you
        r.pause_threshold = 1
        # to let it ignore surrounding sounds 
        r.energy_threshold = 50
        audio = r.listen(source, 0, 4) # 0, 4 is how much time it wait to listen


    try:
        print("Understanding...")
        query = r.recognize_google_cloud(audio, language="en-in")
        print(f"You said: {query}\n")
    except Exception as e:
        print("say that again")
        return "None"
    return query