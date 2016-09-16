# this program takes a list of numbers from input, finds the number of items from the list, then divides
# the numbers added together in the list by the amount of numbers in the list with len()
# outputing an average number for the user
def main():
    print("\nWelcome, this program gives you an average for your numbers. Please enter your numbers, then enter stop when you're finished: \n")

    # defines numbers as a list for later input
    numbers = []

    # this loop repeats itself until the input is "stop" so that the user can submit multiple numbers
    # while True is used to create an infinite loop, because while true is always true
    while True:
        inputnumber = input("Enter a number: ")

        # if the string inputted by the user is "stop", the loop stops
        if inputnumber == "stop":
            break

        # this takes the numbers from input and appends them to the empty list defined as a variable
        # by numbers = [], as floats so that they can be used for an expression that gives the user
        # their average number
        numbers.append(float(inputnumber))

    # this combines a nice string by joining the numbers from the list separated by commas
    # join() joins the numbers in a list for str()
    # map is a function I was shown in Python tutoring to make a better program
    # str() is used so that commas can be used, you can't separate floats with commas
    # (I don't fully understand it's functionality)
    # the sum() function takes the total of all the numbers added together,
    # then len() is used to produce the number used to divide the sum of the numbers
    # from the list added together
    # print() prints this nicely formatted string for the user
    print("\nThe average of", ', '.join(map(str, numbers)) ,"is",sum(numbers)/len(numbers))

main()
