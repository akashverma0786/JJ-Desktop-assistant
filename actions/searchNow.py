import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import webbrowser

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

query = takeCommand().lower()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        # Remove words that we don't want to search
        query = query.replace('jj', '')
        query = query.replace('google search', '')
        query = query.replace('google', '')
        speak("The result is")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 1) # query = query, 1 = no of lines of summary
            speak(result)
        except:
            speak("Sorry, No data found!")

def searchYouTube(query):
    if "youtube" in query:
        speak("This is what I found on YouTube ")
        query = query.replace('jj', '')
        query = query.replace('youtube', '')
        query = query.replace('search', '')
        query = query.replace('youtube search', '')
        # search the query on youtube
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        # Open the first video that appears
        pywhatkit.playonyt(query)
        speak("Done sir!")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("searching in WikipediA")
        query = query.replace('jj', '')
        query = query.replace('wikipedia', '')
        query = query.replace('search', '')
        query = query.replace('wikipedia search', '')
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
