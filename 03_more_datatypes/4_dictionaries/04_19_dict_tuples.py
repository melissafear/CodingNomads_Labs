'''
Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}

unsorted_list=[]
for thing in input_dict:
    mytuple = (thing, input_dict[thing])
    unsorted_list += [mytuple]



def custom_sort(t):
    return t[1] # looks at 2nd item in tuple


unsorted_list.sort(key=custom_sort)

 #print(unsorted_list) #but actually now sorted

sorted_list=unsorted_list

print(sorted_list)

#Done except I don't really understand the sort thing I did