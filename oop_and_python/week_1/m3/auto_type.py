import pyautogui
from time import *

sleep(4)
for a in range(1, 10):
    pyautogui.write("Hello world!", interval=0.25)
    pyautogui.press("enter")
