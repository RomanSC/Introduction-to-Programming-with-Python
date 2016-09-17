# this program is colorful spam

# import time for delay, so user can visually see incrementation
import time
import random

# for terminal text colors, termcolor 1.1.0 was used
# https://pypi.python.org/pypi/termcolor
# $ pip install termcolor
from termcolor import colored

# lit of colors
colors = ['red', 'blue', 'green', 'yellow', 'white']

# defines spammy as the string "spam"
spammy = "spam"

# while loop is for infinite output
while True:
    # wait 6 miliseconds to print
    time.sleep(0.06)

    # print 'spam'
    print(random.choice(colored('spam', colors)))
