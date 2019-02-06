'''
Using a "for-loop", print out all odd numbers from 1-100.



for x in range(1, 100):
    if x % 2 == 1:
        print(x)



list_= ["Monday", "Tuesday", "Wed", "thur", "fri", "sat", "sun"]

for x in list_:
    print(x)


list_= ["Monday", "Tuesday", "Wed", "thur", "fri", "sat", "sun"]

for x in list_:

    if x.startswith("s"):
        print(x.lower())
    if not x.startswith("s"):
        print(x.upper())
'''

list_= ["Monday", "Tuesday", "Wed", "thur", "fri", "sat", "sun"]

for x in list_:

    if x.startswith("s"):
        print(x.lower())
    else:
        print(x.upper())