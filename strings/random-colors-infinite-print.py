# this program is colorful spam

# import random to pull random color from a list
# found random on Stack Overflow
# http://stackoverflow.com/questions/3998908/how-do-i-perform-a-random-event-in-python-by-picking-a-random-variable
import random

# import time
import time

# for terminal text colors, termcolor 1.1.0 was used
# https://pypi.python.org/pypi/termcolor
# $ pip install termcolor
from termcolor import colored

# lit of colors to be used
colors = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan']

# defines spammy as the string "spam"
spammy_1 = "                                                                                "
spammy_2 = "                                                                                "
spammy_3 = "________________________________________________________________________________"
spammy_4 = "_____________________@@@________________________________________________________"
spammy_5 = "________________________________________________________________________________"
spammy_6 = "____________________________________@@@_________________________________________"
spammy_7 = "________________________________________________________________________________"

# while loop is for indefinite run time
while True:

    # delay also found on Stack Overflow, one milisecond is one thousandth
    # of a second
    # http://stackoverflow.com/questions/510348/how-can-i-make-a-time-delay-in-python
    time.sleep(600/1000)

    # seven different colors being defined randomly
    # pulled from list, as covered in class and tutoring
    color1 = random.choice(colors)
    color2 = random.choice(colors)
    color3 = random.choice(colors)
    color4 = random.choice(colors)
    color5 = random.choice(colors)
    color6 = random.choice(colors)
    color7 = random.choice(colors)

    # take the text, color it, then print it to the end of the line
    # without "end=''" text does not fill the entire terminal
    # this makes it "responsive" to the size of the terminal
    # "print(colored('string to be printed', 'red'))"
    # found "end=''" at Stack Overflow as well
    # http://stackoverflow.com/questions/2456148/python-print-end
    # flush=True fixes terminal buffer issues when using time.sleep()
    print(colored(spammy_2, color1), end='__')
    print(colored(spammy_3, color2), end='__')
    print(colored(spammy_4, color3), end='__')
    print(colored(spammy_5, color4), end='__')
    print(colored(spammy_6, color5), end='__')
    print(colored(spammy_7, color6), end='__')
    print(colored(spammy_7, color7), end='__', flush=True)
