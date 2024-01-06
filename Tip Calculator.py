#Python tip calculator
#Input total bill, percentage tip as well as number of people splitting the bill

print('Welcome to the tip calculator!')
totalbill = input('What was the total bill($)?')
tip = input('What percentage tip would you like to give? 10, 12 or 15?')
people = input('How many people to split the bill?')
total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
individual = float(total_amount) / float(people)
individual_amount = round(individual, 2)
print(f'Each person should pay: ${individual_amount}')

#Output Example:
#Welcome to the tip calculator!
#What was the total bill($)?124.56
#What percentage tip would you like to give? 10, 12 or 15?12
#How many people to split the bill?7
#Each person should pay: $19.93

