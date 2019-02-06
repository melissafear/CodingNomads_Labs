'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49


for x in range(0, 50):
    print(x, end=' ')



for x in range(0, 10):
    print(x, end=' ')

print("\r")

for x in range(10, 20):
    print(x, end=' ')

print("\r")

for x in range(20, 30):
    print(x, end=' ')

print("\r")

for x in range(30, 40):
    print(x, end=' ')

print("\r")

for x in range(40, 50):
    print(x, end=' ')

'''

# a loop that goes through 5 times incrementing the values in the inside loop

#make a loop that goes through 10 items

a = 0
b = 10

for i in range(0,5):
    for x in range(a, b):
        print(x, end=' ')
    print("\r")
    a +=10
    b +=10

#done