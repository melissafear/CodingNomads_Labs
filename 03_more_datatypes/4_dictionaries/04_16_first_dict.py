'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}

'''
'''
my_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
print(my_dict)

# create using a loop and some maths


my_dict ={}


my_dict = {1:1, 2:4, 3:9, 4:16}
my_dict[5]=25
print(my_dict)
'''

my_dict = {}
x=1
for x in range (1,11):
    my_dict[x] = x**x

print(my_dict)

#done