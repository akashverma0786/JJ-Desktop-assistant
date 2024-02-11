import pyttsx3
import speech_recognition as sr
from actions.greetme import greetMe
from actions.searchNow import searchGoogle, searchWikipedia, searchYouTube
import requests
from bs4 import BeautifulSoup
import datetime
from actions.dictapp import openwebapp, closeappweb
import os
import pyautogui
from actions.keyboard import volumeUp, volumeDown
import random
import webbrowser
from actions.news import latestNews
from actions.calculator import cal
from actions.whatsapp import sendMessage
from plyer import notification
from pygame import mixer
import speedtest
from actions.userInterface import play_gif
from actions.game import game_play
from actions.focusgraph import focus_graph
from actions.translator import translategl

for i in range(3):
    a = input("enter password to load Jarvis: ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("Welcome, sir! please say [Wake Up] to load me up")
        break
    elif (i == 2 and a != pw):
        exit()

    elif (a != pw):
        print("Try again \n")

play_gif()

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

def alarm(query):
    timeHere = open("alarmtext.txt", "a")
    timeHere.write(query)
    timeHere.close()
    os.startfile("alarm.py")


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

                elif "change password" in query:
                    speak("What's the new password? ")
                    new_pw = input("Enter the new password")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Your password is no changed!")

                elif "scedule my day" in query:
                    tasks = []
                    speak("Do you want to clear old tasks? [please speak yes or no]")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the number of tasks :-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]} \n")
                            file.close()
                    elif "no" in query:
                        no_tasks = int(input("Enter the number of tasks :-"))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]} \n")
                            file.close()

                elif "show my schedule" in query:
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                    notification.notify(
                        title = "My schedule:- ",
                        message = content,
                        timeout = 15
                    )

                elif "Focus mode" in query:
                    a = str(input("Are you sur, You want to enter focus mode: y/n")).lower()
                    if a == "y":
                        speak("Entering the Focus Mode")
                        os.startfile("C:\\Users\\hp\Desktop\\jjAI\\actions\\focusmode.py")
                        exit()
                    else:
                        pass

                elif "Show my focus" in query:
                    focus_graph()

                elif "translate" in query:
                    query = query.replace("jj", "")
                    query = query.replace("please", "")
                    query = query.replace("translate", "")
                    translategl(query)

                # Using pyautogui
                elif "open" in query:
                    query = query.replace("jj", "")
                    query = query.replace("open", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")

                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576 # 1 megabye = 1024 * 1024 bytes
                    download_net = wifi.download()/1048576
                    print(f"upload speed: {upload_net}, Download speed {download_net}")
                    speak(f"Upload speed is {upload_net} and Download speed is {download_net}")

                elif "cricket score" in query:
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text, "html.parser")
                    team1 = soup.find_all(class_ = "cb-over-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-over-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "current score",
                        message = f"{team1} : {team1_score} \n {team2} : {team2_score}",
                        timeout = 10
                    )

                elif "play a game" in query:
                    game_play()

                elif "screenshot" in query:
                    i = 0
                    im = pyautogui.screenshot()
                    im.save(f"ss_{i}.jpg")
                    i += 1

                elif "Click my photo" in query:
                    # super act as pressing windows button and then searching 
                    pyautogui.press("super")
                    pyautogui.typewrite("Camera")
                    pyautogui.press("enter")
                    pyautogui.sleep(3)
                    speak("smile")
                    pyautogui.press("enter")
                
                elif "hello" in query:
                    speak("hello Sir, How are you?")

                elif "i am fine" in query:
                    speak("That's great, sir!")

                elif "How are you?" in query:
                    speak("Perfect sir, How are you?")

                elif "Thank you" in query:
                    speak("You'r welcome, sir!")

                elif "open" in query:
                    openwebapp(query)

                elif "close" in query:
                    closeappweb(query)

                elif "google" in query:
                    searchGoogle(query)

                elif "youtube" in query:
                    searchYouTube(query)

                elif "wikipedia" in query:
                    searchWikipedia(query)

                elif "news" in query:
                    latestNews()

                elif "calculator" in query or "calculate" in query:
                    query = query.replace("jarvis", "")
                    query = query.replace("calculate", "")
                    cal(query)()
                    
                elif "whatsapp" in query:
                    sendMessage()

                elif "set an alarm" in query:
                    print("input time example - hours and minutes and seconds")
                    speak("set the time")
                    a = input("Please tell the time : ")
                    alarm(a)
                    speak("Done, Sir!")

                elif "i am tired" in query:
                    speak("playing your favourite playlist now")
                    a = (1, 2, 3)
                    b = random.choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=mt9xg0mmt28")
                    elif b == 2:
                        webbrowser.open("https://www.youtube.com/watch?v=dTu5dTEzVM4")
                    else:
                        webbrowser.open("https://www.youtube.com/watch?v=v2EYFtXR2kY")

                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video Paused")

                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")

                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")

                elif "volume up" in query:
                    speak("turning the volume up, Sir!")
                    volumeUp()

                elif "volume down" in query:
                    speak("turning the volume down, Sir!")
                    volumeDown()

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
                
                elif "what is the time" in query or "the time" in query:
                    cur_time = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {cur_time}")

                elif "finally sleep" in query:
                    speak("Going to sleep , Sir!")
                    exit()

                elif "remember that" in query:
                    message = query.replace("remember that", "")
                    message = query.replace("jj", "")
                    speak("You want me to remember" + message)
                    remember = open("remember.txt", "a")
                    remember.write(message)
                    remember.close()

                elif "what do you remember" in query or "read me what you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("You told me to" + remember.read())

                elif "shutdown" in query:
                    speak("Are you sure you want to shutdown the system")
                    shutdown = str(input("Do you wish to shutdown you system? y/n: ")).lower()
                    if shutdown == "y":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "n":
                        break
