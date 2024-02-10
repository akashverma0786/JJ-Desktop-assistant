import requests
import json
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def latestNews():
    apiDict = {
        "business": "https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=87fe168393eb41b2a960f6afe6af0eec",
        "entertainment": "https://newsapi.org/v2/top-headlines?country=in&category=entertainment&apiKey=87fe168393eb41b2a960f6afe6af0eec",
        "health": "https://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=87fe168393eb41b2a960f6afe6af0eec",
        "science": "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=87fe168393eb41b2a960f6afe6af0eec",
        "sports": "https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey=87fe168393eb41b2a960f6afe6af0eec",
        "technology": "https://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=87fe168393eb41b2a960f6afe6af0eec"
    }

    content= None
    url = None

    speak("which sector news do you want to listen ? [business], [entertainment], [health], [science], [sports], [technology]")
    field = input("Type the sector you want the news from: ")
    for key, value in apiDict.items():
        if key.lower() in field.lower():
            url = value
            print("Url found")
            print(url)
            break
        else:
            url = True
    if url:
        print("url not found")

    news = requests.get(url).text
    news = json.loads(news)
    speak("Here is the first news: ")

    arts = news["articles"]
    for articles in arts:
        article = articles["title"]
        print(article)
        speak(article)
        print_url = articles["url"]
        print(f"for more info, please visit: {print_url}")

        a = input("[Press 1 to continue] \n [Press any key to stop]")
        if str(a) == "1":
            pass
        else:
            break
        speak("thats all, Sir!")
        
