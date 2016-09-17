# This is indexing a string the easy way from the textbook
# It's funny because this is "easy"-index.py
print("\nThe string being indexed is \"string\", the fourth character of \"string\" is: ")

# Cannot simply print the indexed character position with string[3] in Python 3.5.2
# Outputs this:
# >>> string[3]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'string' is not defined
# >>>

# You have to assign the string to a variable before indexing it:
indexed_string = "string"

# Now you can print the string:
print(indexed_string[3])

