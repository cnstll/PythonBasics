import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import re
import pygame
import time


gmorse_table = {'A': '.-', 'B': '-...', 'C': '-.-.',
                'D': '-..', 'E': '.', 'F': '..-.',
                'G': '--.', 'H': '....', 'I': '..',
                'J': '.---', 'K': '-.-', 'L': '.-..',
                'M': '--', 'N': '-.', 'O': '---',
                'P': '.--.', 'Q': '--.-', 'R': '.-.',
                'S': '...', 'T': '-', 'U': '..-',
                'V': '...-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--.',
                '0': '-----',  '1': '.----',  '2': '..---',
                '3': '...--',  '4': '....-',  '5': '.....',
                '6': '-....',  '7': '--...',  '8': '---..',
                '9': '----.'
                }


def convert_to_morse(string):
    res = ""
    word_list = re.sub(r'[^\w]', ' ',  string).split()
    for string in word_list:
        for c in string:
            if c is not string[:1]:
                res += ' '
            res += gmorse_table.get(c.upper())
        if string is not word_list[-1]:
            res += " / "
    return res

# The all() function returns True if all items
# in an iterable are true, otherwise it returns False
def check_args():
    if len(sys.argv) < 2:
        exit(0)
    nbr_of_args = len(sys.argv)
    for i in range(1, nbr_of_args):
        if all(c.isalnum() or c.isspace() for c in sys.argv[i]):
            pass
        else:
            print("ERROR")
            exit(1)


def make_morse_sing(morse_str):
    pygame.init()
    # beep = pygame.mixer.Sound("beep.wav")
    pygame.mixer.music.load("beep.wav")
    for c in morse_str:
        if (c is '.'):
            pygame.mixer.music.play()
            time.sleep(2)


check_args()
morse_str = ""
nbr_of_args = len(sys.argv)
for i in range(1, nbr_of_args):
    morse_str += convert_to_morse(sys.argv[i])
    if i != nbr_of_args - 1:
        morse_str += ' / '


make_morse_sing(morse_str)
#print(morse_str)