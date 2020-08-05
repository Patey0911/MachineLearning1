from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

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

def imageGrab():
    box = (Cordinates.dinasaur[0]+96,Cordinates.dinasaur[1],Cordinates.dinasaur[0]+100,Cordinates.dinasaur[1]+30)
    image = ImageGrab.grab(box)
    greyImage = ImageOps.grayscale(image)
    a = array(greyImage.getcolors())
    return (a.sum())

def main():
    restartGame()
    while True:
        if(imageGrab()!=367):
            pressSpace()
            time.sleep(0.1)

main()