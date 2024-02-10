import wolframalpha
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolfRamAlpha(query):
    api_key = "GJUEAR-X5WV8V9QGW"
    requester = wolframalpha.Client(api_key)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("The value cannot be calculated")

def cal(query):
    term = str(query)
    term = term.replace("jj", "")
    # term = term.replace("calculate", "")
    term = term.replace("multiply", "*")
    term = term.replace("divide", "/")
    term = term.replace("plus", "+")
    term = term.replace("subtract", "-")

    final = str(term)
    try:
        result = wolfRamAlpha(final)
        print(f"{result}")
        speak(result)

    except:
        speak("The value is not calculable")