'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input:
Result: 4

'''

words= input("Please enter some words: ")
letter= input("Please enter a letter: ")

print("index of letter '"+ str(letter) +"' is " + str(words.find(letter)))
