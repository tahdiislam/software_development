import pyautogui
from time import sleep


n = int(input())
# n = 5
sleep(5)
for i in range(1, n + 1):
    s = ""
    for j in range(1, i + 1):
        # print(j)
        s += "*"
    pyautogui.write(s, interval=0.25)
    pyautogui.press("enter")