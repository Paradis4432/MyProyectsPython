import time
import winsound

import pyautogui
import pydirectinput


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


def cooldown():
    # ghast 6 minutes
    # q 3 minutes
    # shadow clones 15 mins
    seconds = 0
    mins = 0
    hours = 0
    while True:
        seconds = seconds + 1
        if seconds >= 60:
            mins = mins + 1
            seconds = 0
        if mins % 15 == 0 and mins != 0:
            for i in range(1, 5):
                winsound.Beep(1000, 1000)
                print("time to mine, time:")
                print(f"H: {hours} M: {mins} S: {seconds}")
        if mins >= 60:
            print("1 hour")
            print(f"H: {hours} M: {mins} S: {seconds}")
            seconds = 0
            mins = 0
        if hours >= 24:
            print("reseting")
            print(f"H: {hours} M: {mins} S: {seconds}")

        time.sleep(1)

time.sleep(3)
main()
