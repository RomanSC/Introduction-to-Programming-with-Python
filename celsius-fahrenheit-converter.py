# This program converts Celsius to Fahrenheit and back again
def main():
    # where /n is a new line, this was covered in a recent class and I found this on Stack Overflow
    # in python 3 as opposed to 2.7 print is a function there for parenthesis need to be used
    print("\nWelcome to the Celsius to Fahrenheit converter. Please select an option for what you would like to convert:\n1. Celsius > Fahrenheit\n2. Fahrenheit > Celsius\n")
    response = input()

    # everything within this scope was found in the book besides float(). In python 3 as opposed to 2.7
    # you need to change the type from string to a float in order to use input for an expression
    #
    # the if statements are common in multiple programming languages and I experimented with this
    # program to learn how to use if statements
    if response == '1':
        celsius = float(input ("\nWhat is the Celsius temperature? "))
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print("\nThe temperature is " + str(fahrenheit) + " degrees Fahrenheit!\n")

    # the math here is simply the reverse of the math from the previous scope celsius > fahrenheit
    if response == '2':
        fahrenheit = float(input ("What is the Fahrenheit temperature? "))
        celsius = (fahrenheit - 32) * (5.0 / 9.0)
        print("\nThe temperature is " + str(celsius) + " degrees Celsius!\n")
main()

