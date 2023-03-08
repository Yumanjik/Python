import keyboard
from time import sleep
from pyperclip import copy, paste


def hotkey(text: str):
    copy(text)
    keyboard.press_and_release('ctrl + v')


def vvod(text: str):
    buffer = paste()
    hotkey(text)
    copy(buffer)


if __name__ == '__main__':
    while True:

        if keyboard.is_pressed('0'):
            break

        if keyboard.is_pressed('1'):
            sleep(0.1)
            keyboard.press_and_release('backspace')
            sleep(0.01)
            vvod('Понятно')

        if keyboard.is_pressed('2'):
            sleep(0.1)
            keyboard.press_and_release('backspace')
            sleep(0.01)
            vvod('Вопросов нет')


