names_string = input("Enter the players names, seperate them by a comma and space:\n ")
names = names_string.split(", ")

import random
random_integer = random.randint(0, len(names) - 1)
x = int(random_integer)

if random_integer == x:
    print(names[int(x)] + ' is going to buy the meal today!')