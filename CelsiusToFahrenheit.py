# This program converts Celsius to Fahrenheit

def main():
    celsius = input ("What is the Celsius temperature? ")
    celsius = float(celsius)
    fahrenheit = (9.0 / 5.0) * celsius + 32
    print()
    print ("The temperature is " + str(fahrenheit) + " degrees Fahrenheit!")
main()
