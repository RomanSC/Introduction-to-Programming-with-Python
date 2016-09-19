# This program prints the a letter, then the ascii code for that letter
# coloring the output, in an infinite loop

# import colored from termcolor, terminal colors
from termcolor import colored

# Define alphabet in a list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Define colors in a list
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan']

# Define color# as a color from the list
color0 = colors[0]
color1 = colors[1]
color2 = colors[2]
color3 = colors[3]
color4 = colors[4]
color5 = colors[5]

# True evaluates to true always, so while True makes an infinite loop
while True:
    # Print a letter from the alphabet, color it, keep printing to the end of the line.
    # Print a letters ASCII code, color it, keep printing to the end of the line.
    print(colored(alphabet[0], color0), end='')
    print(colored(ord(alphabet[0]), color0), end='')
    print(colored(alphabet[1], color1), end='')
    print(colored(ord(alphabet[1]), color1), end='')
    print(colored(alphabet[2], color2), end='')
    print(colored(ord(alphabet[2]), color2), end='')
    print(colored(alphabet[3], color3), end='')
    print(colored(ord(alphabet[3]), color3), end='')
    print(colored(alphabet[4], color4), end='')
    print(colored(ord(alphabet[4]), color4), end='')
    print(colored(alphabet[5], color5), end='')
    print(colored(ord(alphabet[5]), color5), end='')

# mmmm... beautiful colorful data.

