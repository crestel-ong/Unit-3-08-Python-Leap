#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the leap year program in python


def main():
    # this function tells you of the year you enter is a leap year

    # input
    year_as_string = input("Please enter the year: ")

    try:
        # convert string to integer
        year = int(year_as_string)

        # process and output
        if year % 4 != 0:
            print("{0} is not leap year.".format(year_as_string))
        else:
            if year % 100 != 0:
                print("{0} is a leap year.".format(year_as_string))
            else:
                if year % 400 != 0:
                    print("{0} is not leap year.".format(year_as_string))
                else:
                    print("{0} is a leap year.".format(year_as_string))

    except Exception:
        print("{0} is not an integer.".format(year_as_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
