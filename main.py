import time

import pyautogui
import win32api
import win32con

import plotly.graph_objects as go


def showMousePos():
    X, Y = pyautogui.position()
    print("X: ", X, " Y: ", Y)
    time.sleep(0.25)


def mouseClick(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def upgrade():
    x = 350
    y = 220

    while True:
        showMousePos()
        time.sleep(1)
        mouseClick(x, y)
        if y == 610 - 130:
            y = y + 200
        else:
            y = y + 130

        if y == 940:
            print("clicking")
            mouseClick(1100, 750)
            time.sleep(1)
            y = 220
        mouseClick(x, y)


upgrade()
