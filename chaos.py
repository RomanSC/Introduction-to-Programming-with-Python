# this program demonstrates a chaotic function
def main():
    # prints a nice message for the user
    print("\nThis program demonstrates a chaotic function.\n")

    # asks for user input of a number between 0 and 1, i.e. 0.27
    # then float() converts it to float to be using in the expression
    x = float(input("Enter a number between 0 and 1:\n"))

    # for i in range(10) is a "for loop", it makes the expression
    # inside the scope run 10 times
    # in this particular scope, after the expression runs
    # the result is printed each time
    for i in range(10):
        # if x = 0.27 for example:
        # 0.27 = 3.9 * 0.27 * 1 - 0.27
        x = 3.9 * x * (1 - x)
        # \n prints a new line
        print (x, "\n")
main()
