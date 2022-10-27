# Nedd Chairi Muñoz
# https://github.com/NeddM

import pyautogui
import keyboard

print("""
Pulsa "o" para parar el bot.
Pulsa "i" para reanudar el bot.
Pulsa "p" para salir del bot.
""")


def farmea():
    while True:
        pyautogui.tripleClick()
        if keyboard.is_pressed('o'):
            noFarmea()
            break
        elif keyboard.is_pressed("p"):
            break


def noFarmea():
    while True:
        if keyboard.is_pressed('i'):
            farmea()
            break
        elif keyboard.is_pressed('p'):
            break


if __name__ == "__main__":
    noFarmea()
