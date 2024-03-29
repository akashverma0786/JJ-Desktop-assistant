from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
# from pygame import mixer
# mixer.init()

# Root is screen size
root = Tk()
root.geometry("1000x500")

def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("VoiceAssistant.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    # mixer.music.load("startup.mp3")
    # mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img = img.resize((1000,500))
        img = ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()

play_gif()
root.mainloop()