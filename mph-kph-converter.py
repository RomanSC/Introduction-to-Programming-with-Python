print("\nWelcome to the Miles Per Hour(MPH) to Kilometers per Hour(KPH) converter: \n1. MPH > KPH\n2. KPH > MPH\n")
response = input()

if response == '1':
    mph = input()
    mph = float(mph)
    mph = mph * 1.609344
    print("\n", mph)

if response == '2':
    kph = input()
    kph = float(kph)
    kph = kph / 1.609344
    print("\n", kph)


