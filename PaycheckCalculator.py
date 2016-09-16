def main():

    print("\nWelcome, this program takes your hours for each day and gives you useful information like your total and average pay for the pay period. \n")

    hours_per_day = []

    while 1:
        input_hours = input("Enter a number: ")

        if input_hours == "stop":
            break

        hours_per_day.append(float(input_hours))

main()
