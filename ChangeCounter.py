def main():
    print("Change Counter!")
    print()
    print("Input how many of each coin you have:")

    quarters = input("Quarters:")
    quarters = float(quarters)

    dimes = input("Dimes:")
    dimes = float(dimes)

    nickels = input("Nickels:")
    nickels = float(nickels)

    pennies = input("Pennies:")
    pennies = float(pennies)

    total = quarters * .25 + dimes * .10 + nickels * .05 + pennies * .01

    print()
    print("Your total change is", total)
main()
