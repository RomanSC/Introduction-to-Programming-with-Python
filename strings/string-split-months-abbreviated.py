# This program slices a single large string containing each month, used as a
# lookup table to give the user the requested month for it's number inputted
# by the user.

def main():
    # Defines months abbreviated into one string, to use as a lookup table
    months_table = "JanFebMarAprMayJunJulAugSepOctNovDec"

    # Defines month_number as the as number from user input
    month_number = input("\nEnter the number for the month you would like: ")

    # Defines position to be used for printing the correct month
    # Jan is 0, 1, 2, so: 1 - 1 = 0 * 3 = 2. 2 is "n" in Jan
    position_in_string = (int(month_number) - 1) * 3

    # Takes the months table and uses the expression to get it's
    # position in the string, adding 3 lines, to obtain the abbreviation
    # for later printing.
    month_from_position = months_table[position_in_string:position_in_string + 3]

    # Print the number of the month inputted by the user plus the abbreviated
    # month from the expression, formatted into a nice string for the user
    print("\n" + "Month", month_number, "is", month_from_position + ".\n")

main()
