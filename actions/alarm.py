import pyttsx3
import datetime
import os

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

extractedTime = open("alarmtext.txt", "rt")
time = str(extractedTime.read())
extractedTime.close()

deleteTime = open("alarmtext.txt", "r+")
deleteTime.truncate(0)
deleteTime.close()

def ring(time):
    setTime = str(time)
    timeNow = setTime.replace("jj", "")
    timeNow = setTime.replace("set an alarm", "")
    timeNow = setTime.replace(" and ", ":")
    alarmTime = str(timeNow)
    print(alarmTime)
    while True:
        currentTime = datetime.datetime.now().strftime("%H:%M:%S")
        if currentTime == alarmTime:
            speak("The alarm is ringing, Sir!")
            os.startfile("music.mp3")
        elif currentTime + "00:00:30" == alarmTime:
            exit()

ring(time)
            
        
