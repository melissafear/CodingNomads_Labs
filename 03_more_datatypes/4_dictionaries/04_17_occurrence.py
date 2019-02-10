'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''

'''
add all the letters to a list
go through the list check if they exists in the dictionary
if it doesn't exist, add the key and value of 1
if it exists, increment value by 1
'''


user_input = input("type some words: ")

all_the_words_list = list(user_input.split())
my_list = list(user_input)
my_dict = {}

for key in my_list:
    if my_dict.get(key) == None:
        my_dict[key]=1
    else:
        my_dict[key] += 1

print(my_dict)

#Done