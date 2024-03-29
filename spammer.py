# -*- coding: utf-8 -*-
# you need to install "pyautogui" (pip3 install pyautogui)
# you need to install "essential_generators" (pip install essential-generators)
import pyautogui
import time
import random
from essential_generators import DocumentGenerator


pyautogui.FAILSAFE = False
file = open('text.txt', 'r')
file.close()
message = ''
print('1. Your text\n2. Text with random symbols\n3. Text with random symbols and length\n4. Text from file\n5. Random sentences')
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
    try:
        file = open('text.txt', 'r')
        delay = int(input('Enter character delay in "ms": '))
        delay = float(delay / 1000)
        print('Nice! You have only 5 seconds to select target!')
        lines = file.readlines()
        time.sleep(5)
        for line in lines:
            text = line.strip()
            pyautogui.write(text, interval=delay)
            pyautogui.press('enter')

    finally:
        file.close()
elif choice == 5:
    sentences = int(input('How many sentences ? (1 sentence = 1 message)'))
    delay = int(input('Enter character delay in "ms": '))
    delay = float(delay / 1000)
    print('Nice! You have only 5 seconds to select target!')
    time.sleep(5)
    gen = DocumentGenerator()
    for i in range(sentences):
        pyautogui.write(gen.sentence(), interval=delay)
        pyautogui.press('enter')





