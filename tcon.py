### Python script for converting time, like minutes to seconds, etc. ###
## version 1.1.0
print("Time converter")

# Setting up the variables
selection1 = input("    Convert from days, hours, minutes, or seconds? ")

# Building the functions
## Convert days
def day_conv():
    selection2 = input("    Convert to hours, minutes, or seconds? ")
    if selection2 not in "[HhMmSs]" :
        print("Invalid input! Please enter H, M, or S.")
        exit()

    num1 = float(input("\r    How many days? "))

    if selection2 in "[Hh]" :
        print(round(num1 * 24, 2))
    elif selection2 in "[Mm]" :
        print(round((num1 * 24) * 60, 2))
    elif selection2 in "[Ss]" :
        print(round(((num1 * 24) * 60) * 60, 2))

## Convert hours
def hour_conv():
    selection2 = input("    Convert to days, minutes, or seconds? ")
    if selection2 not in "[DdMmSs]" :
        print("Invalid input! Please enter D, M, or S.")
        exit()

    num1 = float(input("\r    How many hours? "))

    if selection2 in "[Dd]" :
        print(round(num1 / 24, 2))
    elif selection2 in "[Mm]" :
        print(round(num1 * 60, 2))
    elif selection2 in "[Ss]" :
        print(round(num1 * 60 * 60, 2))

## Convert minutes
def min_conv():
    selection2 = input("    Convert to days, hours, or seconds? ")
    if selection2 not in "[DdHhSs]" :
        print("Invalid input! Please enter D, H, or S.")
        exit()

    num1 = float(input("\r    How many minutes? "))

    if selection2 in "[Dd]" :
        print(round((num1 / 24) / 60, 2))
    elif selection2 in "[Hh]" :
        print(round(num1 / 60, 2))
    elif selection2 in "[Ss]" :
        print(round(num1 * 60, 2))

## Convert seconds
def sec_conv():
    selection2 = input("    Convert to days, hours, or minutes? ")
    if selection2 not in "[DdHhMm]" :
        print("Invalid input! Please enter D, H, or M.")
        exit()

    num1 = float(input("\r    How many seconds? "))

    if selection2 in "[Dd]" :
        print(round(((num1 / 60) / 60) / 24, 2))
    if selection2 in "[Hh]" :
        print(round((num1 / 60) / 60, 2))
    elif selection2 in "[Mm]" :
        print(round(num1 / 60, 2))

## Run everything and catch errors
try:
    if selection1 in "[Dd]" :
        day_conv()
    elif selection1 in "[Hh]" :
        hour_conv()
    elif selection1 in "[Mm]" :
        min_conv()
    elif selection1 in "[Ss]" :
        sec_conv()
    else:
        print("Invalid input! Enter H, M, or S.")
    pass
except ValueError as e:
    print("Integers or decimals only.")
    print("Please try again.")
