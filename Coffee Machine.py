Course Requirements
#1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
#a. Check the user’s input to decide what to do next.
#b. The prompt should show every time action has completed, e.g. once the drink is
#dispensed. The prompt should show again to serve the next customer.
#2. Turn off the Coffee Machine by entering “off” to the prompt.
#a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
#the machine. Your code should end execution when this happens.
#3. Print report.
#a. When the user enters “report” to the prompt, a report should be generated that shows
#the current resource values. e.g.
#Water: 100ml
#Milk: 50ml
#Coffee: 76g
#Money: $2.5
#4. Check resources sufficient?
#a. When the user chooses a drink, the program should check if there are enough
#resources to make that drink.
#b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
#not continue to make the drink but print: “Sorry there is not enough water.”
#c. The same should happen if another resource is depleted, e.g. milk or coffee.
#5. Process coins.
#a. If there are sufficient resources to make the drink selected, then the program should
#prompt the user to insert coins.
#b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
#c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
#pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#6. Check transaction successful?
#a. Check that the user has inserted enough money to purchase the drink they selected.
#E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
#program should say “Sorry that's not enough money. Money refunded.”.
#b. But if the user has inserted enough money, then the cost of the drink gets added to the
#machine as the profit and this will be reflected the next time “report” is triggered. E.g.
#Water: 100ml
#Milk: 50ml
#Coffee: 76g
#Money: $2.5
#c. If the user has inserted too much money, the machine should offer change.
#E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
#places.
#7. Make Coffee.
#a. If the transaction is successful and there are enough resources to make the drink the
#user selected, then the ingredients to make the drink should be deducted from the
#coffee machine resources.
#E.g. report before purchasing latte:
#Water: 300ml
#Milk: 200ml
#Coffee: 100g
#Money: $0
#Report after purchasing latte:
#Water: 100ml
#Milk: 50ml
#Coffee: 76g
#Money: $2.5
#b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
#latte was their choice of drin




#My Take
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


#Course Answer
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])







