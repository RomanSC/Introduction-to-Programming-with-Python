# Test to confirm if termcolor module works:
# found some more info on how it works at Stack Overflow
# http://stackoverflow.com/questions/7640133/running-a-python-script-produces-importerror-no-module-named-termcolor/7640171#7640171
from termcolor import colored
print(colored('hello', 'red'), colored('world', 'green'))
