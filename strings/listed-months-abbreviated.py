# This program uses a list as a lookup table containing abbreviated months
# to give the user the month corresponding to it's number.

# I made months-abbreviated.py before completing the example using a list
# from the book, so I'm making a similar app, but not as cool.

def main():
    # A list containing the abbreviated months to be used as a lookup table.
    months_table = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct',
                    'No', 'Dec']

    # Defines month_number as the as number from user input
    month_number = input("\nEnter the number for the month you would like: ")

    # Print the month number plus the abbreviated month from the list, using an
    # expression wrapped within the string to pull the month from the list
    # for output.
    print("\nMonth", month_number, "is", months_table[int(month_number)- 1] + ".\n")

main()
