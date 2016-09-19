# This program uses a list as a lookup table containing abbreviated months
# to give the user the month corresponding to it's number.

# I made months-abbreviated.py before completing the example using a list
# from the book, so I'm making a similar app, but not as cool.

def main():
    # A list containing the abbreviated months to be used as a lookup table.
    months_abbreviated_table = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug',
                                'Sep', 'Oct', 'Nov', 'Dec']
    months_table = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Defines choice for user to input whether they want the full name
    # of the month or it's abbreviation.
    print("Please choose whether you would like the abbreviation for the month or the full name (1/2): \n1. Full name. \n2. Abbreviation. \n")
    choice = input("")


    # Defines month_number as the as number from user input
    month_number = input("\nEnter the number for the month you would like: ")

    # if the user inputs 1 give them the full name
    if choice == '1':
       # Print the month number plus the month from a list, using an
       # expression wrapped within the string to pull the month from the list
       # for output.
       print("\nMonth", month_number, "is", months_table[int(month_number)- 1] + ".\n")

    # if the user inputs 2 give them the abbreviation
    if choice == '2':
        # Print the month number plus the abbreviated month from a list, using an
        # expression wrapped within the string to pull the month from the list
        # for output.
        print("\nMonth", month_number, "is", months_abbreviated_table[int(month_number)- 1] + ".\n")

main()
