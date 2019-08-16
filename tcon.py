#!/usr/bin/python3
### Python script for converting time, like minutes to seconds, etc. ###
tcon_version = "1.7.0"

# Import time!
import sys

# Setting up the variables
try:
    if len(sys.argv[1]) > 0:
        arg_opt = True
        selection1 = sys.argv[1]
except IndexError:
    arg_opt = False
    selection1 = input("    Convert from weeks, days, hours, minutes, or seconds? ")

# Building the functions
## Convert years
def year_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many years? "))
    except Exception as e:
        selection2 = input("    Convert to weeks, days, hours, minutes, or seconds? ")

    if selection2 == "w" :
        # There isn't an exact number of weeks in a year.
        # We get about 52 weeks and 1 day, so this is the first time
        # we're starting out with a float.
        ans1 = round(num1 * 52.18, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "d" :
        ans1 = round((num1 * 52.18) * 7, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "h" :
        ans1 = round(((num1 * 52.18) * 7) * 24, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "m" :
        ans1 = round((((num1 * 52.18) * 7) * 24) * 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "s" :
        ans1 = round(((((num1 * 52.18) * 7) * 24) * 60) * 60, 2)
        print(ans1)
        sys.exit(0)
    else:
        print("Invalid input! Please enter w, d, h, m, or s.")
        sys.exit(1)
## Convert weeks
def week_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many weeks? "))
    except IndexError as e:
        selection2 = input("    Convert to years, days, hours, minutes, or seconds? ")

    if selection2 == "y" :
        ans1 = round(num1 / 52.18, 2)
        if num1 == 52 :
            print("About 1 year minus 1 day")
            sys.exit(0)
        else:
            print(ans1)
            sys.exit(0)
    elif selection2 == "d" :
        ans1 = round(num1 * 7, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "h" :
        ans1 = round((num1 * 7) * 24, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "m" :
        ans1 = round(((num1 * 7) * 24) * 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "s" :
        ans1 = round((((num1 * 7) * 24) * 60) * 60, 2)
        print(ans1)
        sys.exit(0)
    else:
        print("Invalid input! Please enter y, d, h, m, or s.")
        sys.exit(1)

## Convert days
def day_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many days? "))
    except IndexError as e:
        selection2 = input("    Convert to years, weeks, hours, minutes, or seconds? ")

    if selection2 == "y" :
        ans1 = round((num1 / 52.18) / 7, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "w" :
        ans1 = round(num1 / 7, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "h":
        ans1 = round(num1 * 24, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "m":
        ans1 = round((num1 * 24) * 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "s":
        ans1 = round(((num1 * 24) * 60) * 60, 2)
        print(ans1)
        sys.exit(0)
    else :
        print("Invalid input! Please enter y, w, h, m, or s.")
        sys.exit(1)

## Convert hours
def hour_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many hours? "))
    except IndexError as e:
        selection2 = input("    Convert to years, weeks, days, minutes, or seconds? ")

    if selection2 == "y" :
        ans1 = round(((num1 / 24) / 7) / 52.18, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "w" :
        ans1 = round((num1 / 24) / 7 ,2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "d" :
        ans1 = round(num1 / 24, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "m" :
        ans1 = round(num1 * 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "s" :
        ans1 = round(num1 * 60 * 60, 2)
        print(ans1)
        sys.exit(0)
    else:
        print("Invalid input! Please enter y, w, d, m, or s.")
        sys.exit(1)

## Convert minutes
def min_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many minutes? "))
    except IndexError as e:
        selection2 = input("    Convert to years, weeks, days, hours, or seconds? ")

    if selection2 == "y" :
        ans1 = round((((num1 / 52.18) / 7) / 24) / 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "w" :
        ans1 = round(((num1 / 7) / 24) / 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "d" :
        ans1 = round((num1 / 24) / 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "h" :
        ans1 = round(num1 / 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "s" :
        ans1 = round(num1 * 60, 2)
        print(ans1)
        sys.exit(0)
    else:
        print("Invalid input! Please enter y, w, d, h, or s.")
        sys.exit(1)

## Convert seconds
def sec_conv():
    try:
        if arg_opt is True and len(sys.argv[2]) > 0 :
            num1 = float(sys.argv[2])
            if len(sys.argv[3]) > 0 :
                selection2 = sys.argv[3]
        else:
            num1 = float(input("\r    How many seconds? "))
    except IndexError as e:
            selection2 = input("    Convert to years, weeks, days, hours, or minutes? ")

    if selection2 == "y" :
        ans1 = round(((((num1 / 60) / 60) / 24) / 7) / 52.18, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "w" :
        ans1 = round((((num1 / 60) / 60) / 24) / 7, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "d" :
        ans1 = round(((num1 / 60) / 60) / 24, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "h" :
        ans1 = round((num1 / 60) / 60, 2)
        print(ans1)
        sys.exit(0)
    elif selection2 == "m" :
        ans1 = round(num1 / 60, 2)
        print(ans1)
        sys.exit(0)
    else:
        print("Invalid input! Please enter y, w, d, h, or m.")
        sys.exit(1)

def tcon_help():
    print("tcon - A time denomination conversion tool")
    print("Version:", tcon_version)
    print("\nYou can either use the prompts or the following command-line arguments")
    print("Usage: tcon.py <starting denomination> <amount> <desired denomination>")
    print(" y    -    Years")
    print(" w    -    Weeks")
    print(" d    -    Days")
    print(" h    -    Hours")
    print(" m    -    Minutes")
    print(" s    -    Seconds")
    print("\nExample: tcon.py d 1 h")
    print("24.0")
    print("\n2019, Hupmake")
    sys.exit(0)

## Run everything and catch errors
try:
    if selection1 == "y" :
        year_conv()
    elif selection1 == "w" :
        week_conv()
    elif selection1 == "d" :
        day_conv()
    elif selection1 == "h" :
        hour_conv()
    elif selection1 == "m" :
        min_conv()
    elif selection1 == "s" :
        sec_conv()
    elif selection1 == "help" :
        tcon_help()
    elif selection1 == "version" :
        print("Version:", tcon_version)
    else:
        tcon_help()
    pass
except ValueError as e:
    print("Integers or decimals only.")
    print("Please try again.")
    sys.exit(1)
