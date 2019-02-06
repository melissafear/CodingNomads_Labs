'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

# flatten the list - use a loop

#print(starting_list[0][1])

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]

flattened_list = []

for inner_list in starting_list:
    for item in inner_list:
        flattened_list.append(item)

print(flattened_list)

#done