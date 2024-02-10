import pywhatkit
from datetime import datetime, timedelta
import speech_recognition as sr
import pyttsx3
import webbrowser
from bs4 import BeautifulSoup
from time import sleep

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

update = int((datetime.now() + timedelta(minutes=2)).strftime("%M"))
strTime = int(datetime.now().strftime("%H"))

def sendMessage():
    speak("who do you want to message?")
    a = int(input("Press 1 for Person1, Press 2 for Person2, Press 3 for Person3 : "))
    if a == 1:
        speak("What's the message?")
        message = str(input("Enter the message : "))
        pywhatkit.sendwhatmsg("+910987654321", message, time_hour=strTime, time_min=update)
    
    elif a == 2:
        speak("What's the message?")
        message = str(input("Enter the message : "))
        pywhatkit.sendwhatmsg("+910987654321", message, time_hour=strTime, time_min=update)

    elif a == 3:
        speak("What's the message?")
        message = str(input("Enter the message : "))
        pywhatkit.sendwhatmsg("+910987654321", message, time_hour=strTime, time_min=update)