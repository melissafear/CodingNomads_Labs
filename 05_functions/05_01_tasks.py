'''

Write a script that completes the following tasks.

'''


# takes in a number from the user between 1 and 1,000,000,000

# calls a function that determines whether the number is divisible by both 4 and 7

# calls a function that determines whether the number is divisible by 4 or 7

# calls a function that determines whether the number is divisible by 4 or 7 exclusively

# print the results


n = int(input("write a number:  "))

def div_by_4_and_7(n):
    return n % 4 == 0 and n % 7 == 0

def div_by_4_or_7(n):
    return n % 4 == 0 or n % 7 == 0

def div_by_4_only_or_7_only(n):
    return (n % 4 == 0 and not n % 7 == 0) or (n % 7 == 0 and not n % 4 == 0)


print(div_by_4_and_7(n))
print(div_by_4_or_7(n))
print(div_by_4_only_or_7_only(n))


