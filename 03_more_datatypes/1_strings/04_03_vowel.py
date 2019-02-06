'''
Write a script prints the number of times a vowel is used in a user inputted string.

'''

words = input("Please enter some words: ")
wordslower = words.lower()

a = words.count("a") + words.count("A")
e = words.count("e") + words.count("E")
i = words.count("i") + words.count("I")
o = words.count("o") + words.count("O")
u = words.count("u") + words.count("U")

print (a+e+i+o+u)

#done