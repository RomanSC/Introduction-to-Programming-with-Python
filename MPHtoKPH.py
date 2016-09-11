print("Welcome to the Miles Per Hour(MPH) to Kilometers per Hour(KPH) converter:")
print("1. MPH > KPH")
print("2. KPH > MPH")
print()
response = input()
print()

if response == 'MPH':
    mph = input()
    mph = float(mph)
    mph = mph * 1.609344
    print(mph)

if response == 'KPH':
    kph = input()
    kph = float(kph)
    kph = kph / 1.609344
    print(kph)


