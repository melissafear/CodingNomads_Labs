'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''

intNumber = 3
fltNumber = 10.0

print(float(intNumber))

print(int(fltNumber))

print(fltNumber//intNumber)

a = int(input("Please enter a number "))
b = int(input("Please enter another number "))
print(str(a) + " x " + str(b) +" = " + str(a*b))