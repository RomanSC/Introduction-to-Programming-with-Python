print("\nWelcome to the binary to ASCII (text) or ASCII to binary converter. Please type \"Binary\" for binary > ASCII, or \"ASCII\" for ASCII > binary.\n1. Binary > ASCII\n2. ASCII > Binary \n")

response = input()

if response == '1':

    binary = input()

    bytes = binary.split()

    chrs = [chr(int(byte, 2)) for byte in bytes]

    print("".join(chrs))

if response == '2':
	text = input()

	bytes = [format(ord(chr), 'b') for chr in text]

	print(" ".join(bytes))

