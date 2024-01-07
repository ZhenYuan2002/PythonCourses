print('''Welcome to Python Pizza Deliveries!
Here's the Menu for your pizza:
Small pizza: $15
Medium pizza: $20
Large pizza: $25
Add pepperoni for small pizza: +$2
Add pepperoni for medium or large pizza: +$3
Add extra cheese for any size pizza: +$1\n\n\n''')

size = input('What size pizza do you want? S, M, or L\n')
add_pepperoni = input('Do you want pepperoni? Y or N\n')
extra_cheese = input('Do you want extra cheese? Y or N\n')

if size == 'S' and extra_cheese == 'Y' and add_pepperoni == 'Y':
    print('The final bill for your pizza is $18')
elif size == 'S' and extra_cheese == 'N' and add_pepperoni == 'Y':
    print('The final bill for your pizza is $17')
elif size == 'S' and extra_cheese == 'Y' and add_pepperoni == 'N':
    print('The final bill for your pizza is $16')
elif size == 'S' and extra_cheese == 'N' and add_pepperoni == 'N':
    print('The final bill for your pizza is $15')

if size == 'M' and extra_cheese == 'Y' and add_pepperoni == 'Y':
    print('The final bill for your pizza is $24')
elif size == 'M' and extra_cheese == 'N' and add_pepperoni == 'Y':
    print('The final bill for your pizza is $23')
elif size == 'M' and extra_cheese == 'Y' and add_pepperoni == 'N':
    print('The final bill for your pizza is $21')
elif size == 'M' and extra_cheese == 'N' and add_pepperoni == 'N':
    print('The final bill for your pizza is $20')

if size == 'L' and extra_cheese == 'Y' and  add_pepperoni == 'Y':
    print('The final bill for your pizza is $29')
elif size == 'L' and extra_cheese == 'N' and add_pepperoni == 'Y':
    print('The final bill for your pizza is $28')
elif size == 'L' and extra_cheese == 'Y' and add_pepperoni == 'N':
    print('The final bill for your pizza is $26')
elif size == 'L' and extra_cheese == 'N' and add_pepperoni == 'N':
    print('The final bill for your pizza is $25')

print("Thank you for choosing Python Pizza Deliveries!")



#Course Answer
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? "S", "M", or "L"
add_pepperoni = input()  # Do you want pepperoni? "Y" or "N"
extra_cheese = input()  # Do you want extra cheese? "Y" or "N"

# Your code below this line 👇
bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")
