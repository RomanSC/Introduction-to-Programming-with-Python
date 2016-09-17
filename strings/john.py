# When this program is run it's supposed to fail with some sort of error:
# In python shell:
#
# >>> firstandlastName = input("Please enter your full name: ")
# Please enter your name: Jim Mahoney
# Traceback (innermost last):
#   File "<pyshell#8>", line 1, in ?
#       firstandlastName = input("Please enter your full name: ")
#   File "<string>", line 0, in ?
# NameError: Jim Mahoney
#
# I don't get this error using Python 3.5.2 however
# this syntax is fine because Python 3.5.2 raw_input()
# no longer exists and input() accepts input without quotation marks

# sets firstandlastName to user's input for the prompt
firstandlastName = input("Please enter your full name: ")

# prints the full name set to firstandlastName
print(firstandlastName)
