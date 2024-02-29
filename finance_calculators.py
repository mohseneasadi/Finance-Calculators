#financial calculators: this is a program for a small financial company 
#that allows the user to access two different financial calculators:
#an investment calculator and a home loan repayment calculator.

import math

print('-----------------------------------------------------------')
print("investment = to calculate the amount of interest you'll earn on your investment \n" 
        "\nbond = to calculate the amount you'll have to pay on a home loan")
print ('-----------------------------------------------------------')

#users can choose which calculation they want to do first
#The first output that the user sees when the program runs
user_choice = input("Please enter either 'investment' or 'bond' from the menu above to proceed: ")
user_choice = user_choice.lower().strip()
print ('-----------------------------------------------------------')

#check the validity of the user choice
while  user_choice != 'bond' and user_choice != 'investment' :
    print("That's not valid! Please enter just 'bond' or 'investment' ")
    user_choice = input ("Please enter what do you want calculate 'investment' or 'bond': ")
    user_choice = user_choice.lower().strip()
    print('-----------------------------------------------------------')
print("Thank you, Let's start")

print('-----------------------------------------------------------')

# calculate the amount of interest on the investment
if user_choice == 'investment' : 
    deposit = int(input('Please enter the amount of money that you are depositing: '))
    interest_rate = 0.01 * int(input('Please enter the interest rate, a number beetwen 1-100: '))
    years_of_investing = int(input('Please enter the number of years you plan on investing: '))
    kind_of_interest = input('Please enter the kind of interest you want "Simple" or "Compound": ')
    kind_of_interest = kind_of_interest.lower()
    print('-----------------------------------------------------------')

# there is 2 different ways of calculating interest on the investment: simple and compound 
    
    if kind_of_interest == 'simple' :
        total_investment = deposit * (1+ (interest_rate * years_of_investing))
        print(f'Your total investment is {total_investment}')
        print('-----------------------------------------------------------')
    elif kind_of_interest == 'compound' :
        total_investment = deposit * math.pow((1+interest_rate), years_of_investing)
        print(f'Your total investment is {total_investment}')
    else : 
        print("That's not a valid kind of interest")
        print('-----------------------------------------------------------')

# calculate the amount of paying on a home loan
else : 
    house_value = int(input('Please enter the present value of the house: '))
    interest_rate1 = (0.01/12) * int (input('Please enter the annual interest rate, a number beetwen 1-100: '))
    num_of_months = int(input('Please enter the number of months they plan to take to repay the bond: '))
    repayment = ((house_value * interest_rate1)/ (1-(1+interest_rate1)** (-num_of_months)))
    print('-----------------------------------------------------------')
    print(f'Your monthly repayment is {repayment}')
    print('-----------------------------------------------------------')
