def main():
    print("\nChange Counter!\n")
    print("\nInput how many of each coin you have:\n")

    quarters = float(input("Quarters:"))

    dimes = float(input("Dimes:"))

    nickels = float(input("Nickels:"))

    pennies = float(input("Pennies:"))

    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01

    print("\nYou have $%s\n" %(total))
main()
