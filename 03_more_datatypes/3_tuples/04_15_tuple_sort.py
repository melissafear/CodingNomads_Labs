'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

# dig into the tuples to get the number value
# compare the number values
# sort the number values

#TAKE 1!

unsorted_list = [('first_element', 11), ('second_element', 20), ('third_element', 6)]

a_item = unsorted_list[0]
b_item = unsorted_list[1]
c_item = unsorted_list[2]

a = a_item[1]
b = b_item[1]
c = c_item[1]

if a < b and a < c:
    if b < c:
        sorted_list = [a_item, b_item, c_item]
    else:
        sorted_list = [a_item, c_item, b_item]

if b < c and b < a:
    if c < a:
        sorted_list = [b_item, c_item, a_item]
    else:
        sorted_list = [b_item, a_item, c_item]

if c < a and c < b:
    if a < b:
        sorted_list = [c_item, a_item, b_item]
    else:
        sorted_list =[c_item, b_item, a_item]

print(sorted_list)



# TAKE 2! (from here https://www.afternerd.com/blog/python-sort-list/#sort-tuples)

def custom_sort(t):
    return t[1] # looks at 2nd item in tuple

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

unsorted_list.sort(key=custom_sort)

#print(unsorted_list) #but actually now sorted

sorted_list=unsorted_list

print(sorted_list)

#Done

