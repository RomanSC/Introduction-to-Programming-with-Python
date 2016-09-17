# this program takes your coins, adds them together, and outputs your total change

def main():
    print("\nChange Counter!\n")
    print("\nInput how many of each coin you have:\n")

    # for each change type, asks for input of the amount of the coin
    # converts them to floats for expression
    quarters = float(input("Quarters:"))

    dimes = float(input("Dimes:"))

    nickels = float(input("Nickels:"))

    pennies = float(input("Pennies:"))

    # this expression takes the amount for each coin, multiplies it by the value
    # for it's type, while adding the total for each type together to use in the string
    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01

    # nice string for outputting the total to the user, %s inside the string
    # places %(total) inside the string, then the print() function prints to
    # deliver the user their total
    print("\nYou have $%s\n" %(total))
main()
