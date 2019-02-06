'''
Write a script that takes three strings from the user and prints the one with the most characters.

'''

wordsA= input("Please enter some words: ")
wordsB= input("Please enter some more words: ")
wordsC= input("Last time, please enter some words: ")

lenA = len(wordsA)
lenB = len(wordsB)
lenC = len(wordsC)

if (lenA > lenB) and (lenA > lenC):
    print(str(wordsA)+" has most characters")

elif (lenB > lenC) and (lenB > lenA):
    print(str(wordsB)+" has most characters")

elif (lenC > lenA) and (lenC > lenB):
    print(str(wordsC)+" has most characters")

else:
    print(":( There is no clear winner...")

#done