# For hard, user has 5 attempts
# For easy, user has 10 attempts
# You have 10/5 attempts remaining to guess the number
# Make a guess

# If wrong
# Too high/low,
# Guess again
# You have -1 attempts remaining to guess the number
# Make a guess


import random
logo = '''
                                                              
 _____                _____               _   _   _           
|_   _|_ _ ___ ___   |   __|___ _____ ___| |_| |_|_|___ ___   
  | | | | | . | -_|  |__   | . |     | -_|  _|   | |   | . |  
  |_| |_  |  _|___|  |_____|___|_|_|_|___|_| |_|_|_|_|_|_  |  
      |___|_|                                          |___|  

'''
print(logo)
number = random.randint(1, 100)
print('''Welcome to the number guessing game!
I am thinking of a number between 1 to 100.''')
difficultyno = input("I am thinking of a difficulty. Type 'easy' or 'hard'.\n")
difficulty = difficultyno.lower()

if difficulty == 'easy':
    print('You have 10 attempts to guess the number')
    ezguess = int(input('Make a guess'))
    attempts = 9
    while attempts > 0:
        if ezguess > number:
            attempts -= 1
            if attempts == 0:
                print('Sorry, You ran out of guesses.')
                print('The number is ' + str(number))
                break
            else:
                print(f'Too high. You have {attempts} attempts remaining')
                ezguess = int(input('Make a guess'))

        elif ezguess < number:
            attempts -= 1
            if attempts == 0:
                print('Sorry, You ran out of guesses.')
                print('The number is ' + str(number))
                break
            else:
                print(f'Too low. You have {attempts} attempts remaining')
                ezguess = int(input('Make a guess'))

        elif ezguess == number:
            attempts_remaining = str(10 - attempts)
            print(f'Congratulations! You got it in {attempts_remaining} attempts!')
            break

    else:
        print('Sorry, You ran out of guesses.')
        print('The number is ' + str(number))


elif difficulty == 'hard':
    print('You have 5 attempts to guess the number')
    hardguess = int(input('Make a guess'))
    attempts = 5
    while attempts > 0:
        if hardguess > number:
            attempts -= 1
            if attempts == 0:
                print('Sorry, You ran out of guesses.')
                print('The number is ' + str(number))
                break
            else:
                print(f'Too high. You have {attempts} attempts remaining')
                hardguess = int(input('Make a guess'))
        elif hardguess < number:
            attempts -= 1
            if attempts == 0:
                print('Sorry, You ran out of guesses.')
                print('The number is ' + str(number))
                break
            else:
                print(f'Too low. You have {attempts} attempts remaining')
                ezguess = int(input('Make a guess'))
        elif hardguess == number:
            attempts_remaining = str(10 - attempts)
            print(f'Congratulations! You got it in {attempts_remaining} attempts!')
            break
    else:
        print('Sorry, You ran out of guesses.')
        print('The number is ' + str(number))



#Course Answer
from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()
