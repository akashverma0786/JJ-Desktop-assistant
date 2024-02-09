from pynput.keyboard import key, Controller

from time import sleep

keyboard = Controller()
def volumeUp():
    for i in range(3):
        keyboard.press(key.media_volume_up)
        keyboard.release(key.media_volume_up)
        sleep(0.1)

def volumeDown():
    for i in range(3):
        keyboard.press(key.media_volume_down)
        keyboard.release(key.media_volume_down)
        sleep(0.1)
        

