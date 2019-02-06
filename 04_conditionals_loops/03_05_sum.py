'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050

'''
lower = int(input("type a number "))
upper = int(input ("type a higher number ")) + 1

total = 0

for x in range (lower, upper):
    total = total + x
    print(x)


print(total)
