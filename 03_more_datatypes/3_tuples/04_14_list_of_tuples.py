'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

# make a tuple out of a string
# add the tuples to a list


words = "hello world"

wordsplit = words.split()

list_=[]

for word in wordsplit:
    list_.append(tuple(word))

print(list_)

#done
