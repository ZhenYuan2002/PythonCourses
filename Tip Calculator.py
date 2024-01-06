#Python tip calculator


print('Welcome to the tip calculator!')
totalbill = input('What was the total bill($)?')
tip = input('What percentage tip would you like to give? 10, 12 or 15?')
people = input('How many people to split the bill?')
total_amount = ((float(totalbill) * float(tip)) / 100) + float(totalbill)
individual = float(total_amount) / float(people)
individual_amount = round(individual, 2)
print(f'Each person should pay: ${individual_amount}')
