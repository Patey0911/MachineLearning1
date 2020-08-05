from PIL import ImageGrab
import pyautogui
import time

class Cordinates():
    replayBtn = (494,470)
    dinasaur = (264, 461)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.2)
    print("Jump")
    pyautogui.keyUp('space')


restartGame()
while(True):
    time.sleep(1)
    pressSpace()