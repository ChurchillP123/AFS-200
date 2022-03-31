applePrice = 0.50
name = input('Please enter your name: ')
#input from terminal returns a string so result must be casted to an integer
number = int(input(f'Hi {name}. Apples cost ${applePrice:.2f} each. How many would you like to buy? '))
print(f'Thank you {name} for your purchase of {number} apples at a cost of ${applePrice:.2f} each.')
#this print statement is to check that number is indeed an integer and not a string 
print(type(number))
