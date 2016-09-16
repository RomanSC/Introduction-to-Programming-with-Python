def main():
    print("\nWelcome, this program gives you an average for your numbers. Please enter your numbers, then enter stop when you're finished: \n")

    numbers = []

    while 1:
        inputnumber = input("Enter a number: ")

        if inputnumber == "stop":
            break

        numbers.append(float(inputnumber))

    print("\nThe average of", ', '.join(map(str, numbers)) ,"is",sum(numbers)/len(numbers))

main()
