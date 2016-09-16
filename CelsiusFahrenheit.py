def main():
    # This program converts Celsius to Fahrenheit
    print("\nWelcome to the Celsius to Fahrenheit converter. Please select an option for what you would like to convert:\n1. Celsius > Fahrenheit\n2. Fahrenheit > Celsius\n")
    response = input()

    if response == '1':
        celsius = float(input ("\nWhat is the Celsius temperature? "))
        fahrenheit = (9.0 / 5.0) * celsius + 32
        print("\nThe temperature is " + str(fahrenheit) + " degrees Fahrenheit!\n")

    if response == '2':
        fahrenheit = float(input ("What is the Fahrenheit temperature? "))
        celsius = (fahrenheit - 32) * (5.0 / 9.0)
        print("\nThe temperature is " + str(celsius) + " degrees Celsius!\n")
main()

