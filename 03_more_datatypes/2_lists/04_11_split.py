'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.


'''

# get input and make it a list by using split on spaces
# determine which word occurs the most - count the words
# keep track of which word has occured the most times via comparison, store if it is the highest


user_input = input("please write a sentence and I will tell you which word appears the most (but ): ")
all_the_words_list = list(user_input.split())

#print(my_list)

highest_count=0
word = ""
highest_count_word = ""

for word in all_the_words_list:
    current_count =(all_the_words_list.count(word))
    if current_count > highest_count:
        highest_count = current_count
        highest_count_word = word

print(f"'{highest_count_word}' occurs {highest_count} times")

#Done (dpes not handle multiple words of equal highest counts)