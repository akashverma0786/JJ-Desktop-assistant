from pynput.keyboard import Controller, Key

from time import sleep

keyboard = Controller()
def volumeUp():
    for i in range(3):
        keyboard.press(Key.media_volume_up)
        keyboard.release(Key.media_volume_up)
        sleep(0.1)

def volumeDown():
    for i in range(3):
        keyboard.press(Key.media_volume_down)
        keyboard.release(Key.media_volume_down)
        sleep(0.1)
        

