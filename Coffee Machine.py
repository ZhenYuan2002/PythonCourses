
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


#Coffee Machine Project
#Program Requirements:
#	1) Print Report, allows you to show remaining resources, as well as money accumulated
#	2) Check if Resources are sufficient
#	3) Process Coins
#	4) Check if transactions are successful
#	5) Make coffee if transaction is successful
#	6) In process of making coffee, deduct the resources used to make coffee
#Coins: Penny = 1 cent, Dime = 10 cents, Nickel = 5 cents, Quarter = 25 cents
#
#Template:
#What would you like? (espresso/latte/cappuccino):
#There are 4 options, espresso, latte, cappuccino, report
#If report is entered, shows the amount of Water, Milk, Coffee and Money currently in the machine
#For the other 3 options:
#Please insert coins:
#How many quarters?:
#How many dimes?:
#How many nickels?:
#How many pennies?:
#If there is change,
#Here is $change in change.
#Here is you esppresso/latte/cappuccino,Enjoy!
#repeat
resources_left = {"water" : 300, "milk": 200, "coffee": 100}
costofespresso = 1.5
costoflatte = 2.5
costofcappuccino = 3.0
penny = 0.01
dime = 0.10
nickel = 0.05
quarter = 0.25
money = 0
for coffee in MENU:
    while resources_left['water'] >= 50 and resources_left['coffee'] >= 18:
        print('Welcome to the coffee machine!')
        choices = input('What would you like ? Espresso, latte or cappuccino?:')
        choice = choices.capitalize()

        if choice == 'Report':
            print(f'Water: {resources_left["water"]}')
            print(f'Milk: {resources_left["milk"]}')
            print(f'Coffee: {resources_left["coffee"]}')
            print(f'Money: {money}')

        elif choice == 'Espresso':
            print('Please insert coins:')
            nopenny = float(input('How many pennies:'))
            nodime = float(input('How many dimes:'))
            nonickel = float(input('How many nickels:'))
            noquarter = float(input('How many quarters:'))
            totalinput = nopenny + nodime + nonickel + noquarter
            if totalinput == costofespresso:
                money += totalinput
                print(f"Here's your {choice}! Enjoy!")
                resources_left['water'] = resources_left['water'] - 50
                resources_left['coffee'] = resources_left['coffee'] - 18
            elif totalinput > costofespresso:
                change = totalinput - costofespresso
                print(f"Here is ${change} in change")
                money += costofespresso
                print(f"Here's your {choice}! Enjoy!")
                resources_left['water'] = resources_left['water'] - 50
                resources_left['coffee'] = resources_left['coffee'] - 18
            elif totalinput < costofespresso:
                print(f"The amount inserted is insufficient. here is {totalinput} in refunds.\n Please try again")




        elif choice == 'Latte':
           if resources_left['milk'] < 150:
               print('Sorry! We ran out of milk. Try again next time.')
               break
           print('Please insert coins:')
           nopenny = float(input('How many pennies:'))
           nodime = float(input('How many dimes:'))
           nonickel = float(input('How many nickels:'))
           noquarter = float(input('How many quarters:'))
           totalinput = nopenny + nodime + nonickel + noquarter
           if totalinput == costoflatte:
               money += totalinput
               print(f"Here's your {choice}! Enjoy!")
               resources_left['water'] = resources_left['water'] - 200
               resources_left['milk'] = resources_left['milk'] - 150
               resources_left['coffee'] = resources_left['coffee'] - 24
           elif totalinput > costoflatte:
               change = totalinput - costoflatte
               print(f"Here is ${change} in change")
               money += costoflatte
               print(f"Here's your {choice}! Enjoy!")
               resources_left['water'] = resources_left['water'] - 200
               resources_left['milk'] = resources_left['milk'] - 150
               resources_left['coffee'] = resources_left['coffee'] - 24
           elif totalinput < costoflatte:
               print(f"The amount inserted is insufficient. here is {totalinput} in refunds.\n Please try again")


        elif choice == 'Cappuccino':
            if resources_left['milk'] < 100:
                print('Sorry! We ran out of milk. Try again next time.')
                break
            print('Please insert coins:')
            nopenny = float(input('How many pennies:'))
            nodime = float(input('How many dimes:'))
            nonickel = float(input('How many nickels:'))
            noquarter = float(input('How many quarters:'))
            totalinput = nopenny + nodime + nonickel + noquarter
            if totalinput == costofcappuccino:
                money += totalinput
                print(f"Here's your {choice}! Enjoy!")
                resources_left['water'] = resources_left['water'] - 250
                resources_left['milk'] = resources_left['milk'] - 100
                resources_left['coffee'] = resources_left['coffee'] - 24
            elif totalinput > costofcappuccino:
                change = totalinput - costofcappuccino
                print(f"Here is ${change} in change")
                money += costofcappuccino
                print(f"Here's your Cappuccino! Enjoy!")
                resources_left['water'] = resources_left['water'] - 250
                resources_left['milk'] = resources_left['milk'] - 100
                resources_left['coffee'] = resources_left['coffee'] - 24
            elif totalinput < costofcappuccino:
                print(f"The amount inserted is insufficient. here is {totalinput} in refunds.\n Please try again")

    else:
        if resources_left['water'] < 50:
            print(f'We ran out of water. Try again next time')
            break
        elif resources_left['coffee'] < 18:
            print(f'We ran out of coffee. Try again next time')
            break









