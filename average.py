def main():
    print()
    print("Welcome, this program gives you an average for your numbers. Please enter your numbers, then enter stop when you're finished: ")
    print()

    numbers = []

    while 1:
        inputnumber = input("Enter a number: ")

        if inputnumber == "stop":
            break

        numbers.append(float(inputnumber))

    print()

    print("The average of", ', '.join(map(str, numbers)) ,"is",sum(numbers)/len(numbers))

main()
