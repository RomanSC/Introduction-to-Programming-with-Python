# this program demonstrates string indexing
# where 0 is the first character in a given string

# welcome message, and prompt the user for the character to be indexed
character_to_index = input("\nWelcome, this program demonstrates string indexing using Python. \n\nPlease enter a single character to index, for example \"j\": ")

# name the string to be indexed with a variable,
# in this case the string to be indexed will also be
# determined by user input, use \n for new line
indexed_string = input("\nPlease enter a single word containing the letter you just entered: ")

# print the inputted character, with a new line using \n,
# in a nice sentence, with the word to be indexed
# "/n" + rather than "/n", is used because the comma in "\n",
# produces a space in the output that messes up the format
print("\n" + character_to_index + "'s place in the word ", indexed_string, "is: ")

# change indexed string to float and add 1, so that the number
# for the indexed string is "correct", i.e. 0, 1, 2, becomes 1, 2, 3,
# I found the .index operator on Stack Overflow:
# http://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
result = indexed_string.index(character_to_index) + 1

# print the "formatted" position of the character input by the user
print("\n" + str(result))


