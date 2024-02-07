import pyttsx3
import speech_recognition as sr
from greetme import greetMe
from searchNow import searchGoogle, searchWikipedia, searchYouTube
import requests
from bs4 import BeautifulSoup
import datetime

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

if __name__ == "__main__":
    while True:
        query = takeCommand().lower() # LOWER TO WRITE OUR FURTHER QUERIES
        if "wake up" in query:
            greetMe()

            while True:
                query = takeCommand()
                if "go to sleep" in query:
                    speak("Ok sir, You can call me anytime!")
                    break
                
                elif "hello" in query:
                    speak("hello Sir, How are you?")

                elif "i am fine" in query:
                    speak("That's great, sir!")

                elif "How are you?" in query:
                    speak("Perfect sir, How are you?")

                elif "Thank you" in query:
                    speak("You'r welcome, sir!")

                elif "google" in query:
                    searchGoogle(query)

                elif "youtube" in query:
                    searchYouTube(query)

                elif "wikipedia" in query:
                    searchWikipedia(query)

                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")

                elif "weather" in query:
                    search = "weather in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    weather = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {weather}")
                
                elif "what is the time" in query:
                    cur_time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {cur_time}")

                elif "finally sleep" in query:
                    speak("Going to sleep , Sir!")
                    exit()