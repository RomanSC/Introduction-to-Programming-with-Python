# This program is an example of a login system using Python 3.5.2
def pylogin():

    # Imports
    from sys import *

    # hashlib, for sha512, there may be a better choice, probably a one way hash
    # https://docs.python.org/3/library/hashlib.html
    import hashlib, binascii

    registered_or_not = input("\nWelcome. Please login or register a new user: \n1. Login\n2. Register")

    for
    if registered_or_not == '1':
        username_input = input("\nUsername: ")
        password_input = input("\nPassword: ")

    if registered_or_not == '2':
        def register()
            print("Let's make you a new account: ")

            new_user_first_name = new_user_first_name.lower(input("\nPlease enter your first name: "))
            new_user_last_name = new_user_last_name.lower(input("Please enter your last name: "))

            new_user_password = input("\nNow please enter a character that's at least 8 characters, contains a number, a capital letter, and a special character. Preferably an obscure sentence with an uncommon set of words: ")

            # Os.urandom to be used to salt password
            salt = os.urandom

            # Hash the password and salt it
            salted = hashlib.pbkdf2_hmac('sha512', b'new_user_password', b'salt', 100000)

            # Store password

            # Go back to beginning
            pylogin()
        register()
pylogin()


