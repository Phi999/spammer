# -*- coding: utf-8 -*-
# you need to install "pyautogui" (pip3 install pyautogui)
import pyautogui
import time
import random
pyautogui.FAILSAFE = False

file = open('text.txt', 'r')
file.close()
message = ''
print('1. Your text\n2. Text with random symbols\n3. Text with random symbols and length\n4. Text from file')
choice = int(input('Choose an option: '))
if choice == 1:
    message = str(input('Enter your message: '))
    delay = int(input('Enter spam delay in "ms": '))
    delay = float(delay / 1000)
    count = int(input('How many messages? '))

    print('Nice! You have only 5 seconds to select target!')
    time.sleep(5)

    for i in range(count):
        str(pyautogui.write(message))
        pyautogui.press('enter')
        time.sleep(delay)

elif choice == 2:
    length = int(input('Enter message length: '))
    symbols = str(input('Enter your symbols (only english, numbers and other symbols) '))
    delay = int(input('Enter spam delay in "ms": '))
    delay = float(delay / 1000)
    count = int(input('How many messages? '))

    print('Nice! You have only 5 seconds to select target!')
    time.sleep(5)

    for i in range(count):
        message = ''
        for q in range(length):
            message += random.choice(symbols)
        str(pyautogui.write(message))
        pyautogui.press('enter')
        time.sleep(delay)

elif choice == 3:
    n = int(input('Enter the maximum length of the text: '))
    length = range(1, n)
    symbols = str(input('Enter your symbols (only english, numbers and other symbols) '))
    delay = int(input('Enter spam delay in "ms": '))
    delay = float(delay / 1000)
    count = int(input('How many messages? '))

    print('Nice! You have only 5 seconds to select target!')
    time.sleep(5)

    for i in range(count):
        message = ''
        for q in range(random.choice(length)):
            message += str(random.choice(symbols))
        str(pyautogui.write(message))
        pyautogui.press('enter')
        time.sleep(delay)

elif choice == 4:
    file = open('text.txt', 'r')
    n = int(input('Enter the maximum length of the text (recommended: 1000): '))
    length = range(1, n)
    delay = int(input('Enter spam delay in "ms": '))
    delay = float(delay / 1000)
    count = int(input('How many messages? (recommended: 1000): '))
    print('Nice! You have only 5 seconds to select target!')
    time.sleep(5)
    lines = file.readlines()
    for line in lines:
        text = line.strip()
        message = ''
        message += str(text)
        pyautogui.write(message)
        pyautogui.press('enter')
        time.sleep(delay)

    file.close()
