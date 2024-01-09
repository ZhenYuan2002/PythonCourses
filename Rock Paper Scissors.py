rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
playerchoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n'))
#the code 'print(input(value)) renders the value a none type
#the code 'input(value) renders the value a str type
if playerchoice == 0:
    print(rock)
elif playerchoice == 1:
    print(paper)
elif playerchoice == 2:
    print(scissors)

import random
computerchoice = random.randint(0,2)
if computerchoice == 0:
    print('Computer choose rock!\n' + rock)
elif computerchoice == 1:
    print('Computer choose paper!\n' + paper)
elif computerchoice == 2:
    print('Computer choose scissors!\n' + scissors)

choice = [playerchoice, computerchoice]

if playerchoice == computerchoice:
    print('Draw!')
elif playerchoice == 0 and computerchoice == 1:
    print('You lose!')
elif playerchoice == 1 and computerchoice == 0:
    print('You win!')
elif playerchoice == 2 and computerchoice == 1:
    print('You win!')
elif playerchoice == 1 and computerchoice == 2:
    print('You lose!')
elif playerchoice == 2 and computerchoice == 0:
    print('You lose!')
elif playerchoice == 0 and computerchoice == 2:
    print('You win!')

