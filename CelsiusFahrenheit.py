# This program converts Celsius to Fahrenheit
print("Welcome to the Celsius to Fahrenheit converter. Please select an option for what you would like to convert:")
print("1. Celsius > Fahrenheit")
print("2. Fahrenheit > Celsius")
print()
response = input()
print()

if response == '1':
    celsius = input ("What is the Celsius temperature? ")
    celsius = float(celsius)
    fahrenheit = (9.0 / 5.0) * celsius + 32
    print()
    print("The temperature is " + str(fahrenheit) + " degrees Fahrenheit!")

if response == '2':
    fahrenheit = input ("What is the Fahrenheit temperature? ")
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * (5.0 / 9.0)
    print()
    print("The temperature is " + str(celsius) + " degrees Celsius!")


