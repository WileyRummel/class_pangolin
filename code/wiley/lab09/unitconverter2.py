#lab09 version 2 
#now adding support for units: feet, miles, meters, and kilometers.
print("Welcome to Unit Converter! \nThis will tell you how many meters are in your distance!")

while True:
    try:
        var1 = float(input("What is the distance? "))
        var2 = input("What are the units ")
        if var2.lower() == "ft" or var2.lower() == "feet":
            var1 *= .3048
            print(str(var1) + " meters.")
            break
        elif var2.lower() == "mi" or var2.lower() == "miles":
            var1 *= 1609.344
            print(str(var1) + " meters.")
            break
        elif var2.lower() == "m" or var2.lower() == "meters" or var2.lower() == "meter":
            print(str(var1) + " Meters... DUH!")
            break
        elif var2.lower() == "km" or var2.lower() == "kilometers" or var2.lower() == "kilometer":
            var1 *= 1000
            print(str(var1) + " meters")
            break
    except ValueError:
            print("Must be a number distance and the units must either kilometers, meters, miles, or feet. ")