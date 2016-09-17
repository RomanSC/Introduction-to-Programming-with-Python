# this program demonstrates string indexing
# where 0 is the first character in a given string

# welcome message, and prompt the user for the character to be indexed
character_to_index = input("\nWelcome, this program demonstrates string indexing using Python.\nPlease input a single character to index, for example \"j\": ")

# name the string to be indexed with a variable,
# in this case the string to be indexed will
# also be determined by user input
indexed_string = input("Please input a single word containing the letter you just entered: ")

# print the indexed string, with a new line using \n
print(character_to_index, "'s place in the word ", indexed_string, "is: ")

# print the position of the character input by the user
# I found the .index operator on Stack Overflow:
# http://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
print(indexed_string.index(character_to_index))


