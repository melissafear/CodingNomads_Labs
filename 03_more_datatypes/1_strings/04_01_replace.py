'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

words= input("Please enter some text: ")
symbol= input("Please enter a symbol: ")

'''
#TAKE 1
targetCharacter = words[0].lower()
newWords = words.replace(targetCharacter, symbol)

targetCharacter = words[0].upper()
newWords = newWords.replace(targetCharacter, symbol)s
print(newWords)
'''
'''
#TAKE2
targetCharacterLower = words[0].lower()
targetCharacterUpper = words[0].upper()

newWords = words\
    .replace(targetCharacterLower, symbol)\
    .replace(targetCharacterUpper, symbol)
print(newWords)
'''
#'''
#TAKE3

targetCharacter = words[0]


newWords = words\
    .replace(targetCharacter.upper(), symbol)\
    .replace(targetCharacter.lower(), symbol)
#'''

print(newWords)


