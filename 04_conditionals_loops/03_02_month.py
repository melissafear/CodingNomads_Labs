'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''

month = input("enter a number between 1 - 6: ")

if not month.isdigit():
    print("not a number")

else:
    month = int(month)

    if month > 12 or month < 1:
        print("not a month number")

    elif month == 1:
        print("January")

    elif month == 2:
        print("February")

    elif month == 3:
        print("March")

    elif month == 4:
        print("April")

    elif month == 5:
        print("May")

    elif month == 6:
        print("June")
