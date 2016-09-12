def main():
    print("Welcome, this program calculates the value of an investment: ")
    print()

    principal = input("Please enter the principal: ")
    principal = float(principal)

    apr = input("Enter the annual interest rate: ")
    apr = float(apr)

    years = input("Enter the years: ")
    years = int(years)

    for i in range(years):
        principal = principal * (1 + apr)

        print(principal)
main()
