import pydirectinput
import pyautogui
import time


def moveRight():
    pyautogui.move(-300, 0)
    pyautogui.move(-300, 0)
    pyautogui.move(-300, 0)
    pyautogui.move(-300, 0)
    pyautogui.move(-250, 0)


def holdMouse():
    pydirectinput.mouseDown()


def pressQ():
    pydirectinput.keyDown('q')
    pydirectinput.keyUp('q')


def moveUp():
    pydirectinput.keyDown('space')
    time.sleep(2)
    pydirectinput.keyUp('space')


def moveDown():
    pydirectinput.keyDown('shift')
    time.sleep(4)
    pydirectinput.keyUp('shift')


def pressW():
    pydirectinput.keyDown('w')


def pressD():
    pydirectinput.keyDown('d')


time.sleep(2)  # so u can switch to your game


def main():
    pressD()
    holdMouse()
    cont = 0
    laps = 0

    while True:
        holdMouse()
        pressD()
        time.sleep(9)
        pressQ()
        time.sleep(9)
        moveRight()
        cont = cont + 1
        print(cont, "cont plus")
        if cont == 3:
            cont = 0
            if laps == 2:
                laps = 0
                moveDown()
                continue
            moveUp()
            laps = laps + 1
            print(laps, "laps plus")

main()

def test():
    moveUp()
    moveUp()
    time.sleep(1)
    moveDown()
