# This program repetitively prints code smell into the terminal

import time

import random

from termcolor import colored

code_smell = ['color0 = colors[0]', 'Using successive names like this.', ' ...misses the point of the list itself.', 'color1 = colors[1]', 'color2 = colors[2]', 'color3 = colors[3]', 'color4 = colors[4]', 'color5 = colors[5]', 'print(colored(alphabet[0], color0), end='')', 'print(colored(ord(alphabet[0]), color0), end='')', 'print(colored(alphabet[1], color1), end='')', 'print(colored(ord(alphabet[1]), color1), end='')', 'print(colored(alphabet[2], color2), end='')', 'print(colored(ord(alphabet[2]), color2), end='')', 'print(colored(alphabet[3], color3), end='')', 'print(colored(ord(alphabet[3]), color3), end='')', 'print(colored(alphabet[4], color4), end='')', 'print(colored(ord(alphabet[4]), color4), end='')', 'print(colored(alphabet[5], color5), end='')', 'print(colored(ord(alphabet[5]), color5), end='')']

colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan']

# Can't use "for color_number in range(10)" because it's predictable,
# a loop however does make better code, like this
while True:

    # Delay in miliseconds, a milisecond is one thousandth of a second
    #time.sleep(10/1000)

    random_color_number = random.choice(colors)

    random_code_smell = random.choice(code_smell)

    print(colored(random_code_smell, random_color_number), end='', flush=True)

    #for list_items in range(5):
    #    character = chr(ord(code_smell) + list_items)
    #    for ascii_of_list_items in (ord(character), character):
    #        print(colored(ascii_of_list_items, colors[list_items]), end='')




