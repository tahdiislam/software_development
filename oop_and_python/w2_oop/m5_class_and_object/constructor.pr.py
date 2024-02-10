from time import sleep
import pyautogui


class Pen:
    manufactured = "Bangladesh"

    def __init__(self, brand, owner, color, price):
        self.brand = brand
        self.owner = owner
        self.color = color
        self.price = price

    def write(self, text):
        sleep(5)
        pyautogui.write(text, interval=0.25)


my_pen = Pen("matador", "me", "black", "10")
print(my_pen.owner, my_pen.brand, my_pen.color, my_pen.price)
my_pen.write("something")
