
def main():
    print("\nWelcome, this program calculates the value of an investment: \n")

    principal = float(input("Please enter the principal: "))

    apr = float(input("Enter the annual interest rate: "))

    years = int(input("Enter the years: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("\n", principal)

main()
