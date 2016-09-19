# This is a program to generate usernames
def main():

    # A nice welcome
    print("\nWelcome, this is a program to generate usernames.")

    # The following two lines for user input
    first_name = input("\nPlease input your first name: ")

    last_name = input("\nPlease input your last name: ")

    # In Python 3.5.2 the lowercase module doesn't exist
    # So I found the built-in function on Stack Overflow
    # converting first_name and last_name to lowercase
    # improves upon this code where it's lacking
    # (before input() would prompt the user to enter
    # in lowercase)
    # http://stackoverflow.com/questions/16643166/string-lower-in-python-3
    first_name = first_name.lower()

    last_name = last_name.lower()

    # Concatenate the first letter of first_name,
    # With last_name to produce the username
    user_name = first_name[0] + last_name[:7]

    print("\nYour username is:", user_name, "\n")

main()
