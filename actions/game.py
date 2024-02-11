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

def game_play():
    speak("lets play")
    i = 0
    my_score = 0
    comp_score = 0

    while (i < 5):
        print("Lets play together, Rock, paper and scissors")
        choose = ("rock", "paper", "scissors")
        comp_choose = random.choice(choose)
        query = takeCommand().lower()
        if (query == "rock"):
            if (comp_choose == "rock"):
                speak("rock")
                print("Tie!")
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            elif (comp_choose == "paper"):
                speak("Paper")
                comp_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            else:
                speak("scissors")
                my_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")

        elif (query == "paper"):
            if (comp_choose == "rock"):
                speak("rock")
                my_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            elif (comp_choose == "paper"):
                speak("Paper")
                print("Tie!")
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            else:
                speak("scissors")
                comp_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")

        elif (query == "scissors" or query == "scissor" or query == "Caesar"):
            if (comp_choose == "rock"):
                speak("rock")
                comp_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            elif (comp_choose == "paper"):
                speak("Paper")
                my_score += 1
                i += 1
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
            else:
                speak("scissors")
                print("Tie!")
                print(f"Score : \n ME: {my_score} \n JJ: {comp_score}")
    print(f"Final score: \n ME: {my_score} \n JJ: {comp_score}")
    if my_score > comp_score:
        print("You win")
        speak("You win, Sir! Congratulations on your victory!")
    else:
        print("You Loose!")
        speak("Better luck next time, Sir!")


