import pyautogui,time,os

time.sleep(4)
f = open("spamText.txt","r")
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
