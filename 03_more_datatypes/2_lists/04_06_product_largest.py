'''
Take in 10 numbers from the user. Place the numbers in a list.
Calculate the product of all of the numbers in the list.
Also, find the largest number in the list.


hint use splits method

'''
numbers = input("Enter 10 numbers with a comma between them ")
numbers = numbers.split(",")


#a,b,c,d,e,f,g,h,i,j=numbers.split(",")

#product = numbers[0] * numbers[1]* numbers[2] * numbers[3] * numbers[4]\
# * numbers[5] * numbers[6] * numbers[7] * numbers[8] * numbers[9]

product = 1
for eachnumber in numbers:
    product = int(eachnumber) * product
    #print(int(eachnumber))

print(f"product:{product}")

print(f"max number: {max(numbers)}")


#done


