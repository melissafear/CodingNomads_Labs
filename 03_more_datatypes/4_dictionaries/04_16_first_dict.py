'''
Write a script that creates a dictionary of keys, n and values n*n for numbers 1-10. For example:

result = {1: 1, 2: 4, 3: 9, ...and so on}


'''

my_dict = {}
x=1
for x in range (1,11):
    my_dict[x] = x**x

print(my_dict)

#done