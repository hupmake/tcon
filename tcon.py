### Python script for converting time, like minutes to seconds, etc. ###

print("Time converter v1.0.0")

# Setting up the variables
selection1 = input("    Convert from hours, minutes, or seconds? ")
selection2 = input("    Convert to hours, minutes, or seconds? ")

## Debugging
#print(selection1)
#print(selection2)

# Building the functions
## Convert hours to minutes
def hour_conv():
    global selection2
#    print(selection2)
    num1 = float(input("\r How many hours? "))
#    print(num1)
## This shiz is broken
    if selection2 == "m" or selection2 == "M":
        print(num1 * 60.0)
    elif selection2 == "s" or selection2 == "S":
        print(num1 * 60.0 * 60.0)

def min_conv():
    global selection2

    num1 = float(input("\r How many minutes? "))

    if selection2 == "h" or selection2 == "H":
        print(num1 / 60.0)
    elif selection2 == "s" or selection2 == "S":
        print(num1 * 60.0)

def sec_conv():
    global selection2

    num1 = float(input("\r How many seconds? "))

    if selection2 == "h" or selection2 == "H":
        print((num1 / 60) / 60)
    elif selection2 == "m" or selection2 == "M":
        print(num1 / 60)

if selection1 == "h" or selection1 == "H":
    hour_conv()
elif selection1 == "m" or selection1 == "M":
    min_conv()
elif selection1 == "s" or selection1 == "S":
    sec_conv()
