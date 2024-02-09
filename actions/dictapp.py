import os
# pyautogui helps you press any keyboard key
import pyautogui
import webbrowser
import pyttsx3


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

dictapps = {
    "commandprompt": "cmd",
    "brave": "brave",
    "vscode": "vscode",
    "pycharm": "pycharm",
    "sublime": "sublime"
}

def openwebapp(query):
    speak("Launching, sir!")
    if ".com" in query or ".in" in query or ".org" in query:
        query = query.replace("open", "")
        query = query.replace("search", "")
        query = query.replace("jj", "")
        query = query.replace("launch", "")
        webbrowser.open(f"https://www.{query}")
    else:
        keys = list(dictapps.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapps[app]}")

def closeappweb(query):
    if "close tab" in query:
        speak("closing sir!")
        pyautogui.hotkey("ctrl", "w")
    elif "close app" in query: # Closes the current app you are on
        speak("Closing, app sir!")
        pyautogui.hotkey("alt", "F4")
    else:
        keys = list(dictapps.key())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapps[app]}.exe")
        