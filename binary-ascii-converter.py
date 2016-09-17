# this program takes an ascii or binary string and converts it

# print a nice welcome message, \n is a new line
print("\nWelcome to the binary to ASCII (ascii_text) or ASCII to binary converter. Please type \"Binary\" for binary > ASCII, or \"ASCII\" for ASCII > binary.\n1. Binary > ASCII\n2. ASCII > Binary \n")

# make a variable for user choice to select the option
choice = input()

# if user selects option 1, ask for input of binary to convert to text/ascii
if choice == '1':
    binary = input()

    bytes = binary.split()

    chrs = [chr(int(byte, 2)) for byte in bytes]

    print("".join(chrs))

# if user selects option 2, ask for input of text/ascii to convert to binary
if choice == '2':
    ascii_text = input()

    bytes = [format(ord(chr), 'b') for chr in ascii_text]

    print(" ".join(bytes))

