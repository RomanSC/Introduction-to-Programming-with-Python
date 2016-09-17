# this program demonstrates one way you could handle passwords in Python 3.5.2

# learned this from here:
# http://www.dreamsyssoft.com/python-scripting-tutorial/ifelse-tutorial.php

# define password as a function, so that this could be used in other
# applications using import
def password():
    # import time for later use, only necessary if you want
    # a delay before the program prints then exits
    import time

    # the password is secret defined by a variable
    thePassword = "secret"

    # take user input; prompt for password
    inputPassword = input("\nPassword: ")

    # take user input; prompt for password
    # if user inputted password was correct do this
    if inputPassword == thePassword:
            print("\nAuthorization successful: ")

    # if not or else, wait 1 seconds then print
    else:
            time.sleep(1)

            print("\nGet out.")

            print("\nNow. ")

            exit()
password()
