'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''

principalAmount = int(input("Please enter an amount to invest: "))
interestRate = int(input("Enter an interest rate in %: "))/100
years = int(input("Enter how many years you have to invest: "))

totalAmount = round(principalAmount*(1+interestRate/1)**years, 2)
compoundEarnings = totalAmount-principalAmount


print("After " + str(years) + " years, you will have earned " + str(compoundEarnings) + " in compound interest, and will have a total of " + str(totalAmount))
