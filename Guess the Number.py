#Write a programme that allows the user to guess the correct number
#My take, the programme has 5 guesses
import random
name = input('Hello, what is your name?\n')
print(f'Hello, {name}! Welcome to Guess the number!')
number = random.randint(1, 20)
print(f'I am thinking of a number between 1 to 20.\nTake a guess.')
guess = int(input())
guesses_remaining = 4
while guess != number:
    if guess != number and guess < number:
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f'Sorry, you ran out of guesses :(\nThe number I was thinking of was {number}')
            break
        else:
            print(f'Ha! Your guess is too low!\nTry again, you have {guesses_remaining} guesses left.')
            guess = int(input())

    elif guess != number and guess > number and guess <= 20:
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f'Sorry, you ran out of guesses :(\nThe number I was thinking of was {number}')
            break
        else:
            print(f'Ha! Your guess is too high!\nTry again, you have {guesses_remaining} guesses left. ')
            guess = int(input())

    elif guess > number:
        guesses_remaining -= 1
        if guesses_remaining == 0:
            print(f'Sorry, you ran out of guesses :(\nThe number I was thinking of was {number}')
            break
        else:
            print(f'Please enter a number between 1 to 20!\nTry again, you have {guesses_remaining} guesses left.')
            guess = int(input())
else:
    print(f'Congratulations! You guessed my number! You got it in ' + str(5 - int(guesses_remaining)) + ' tries!')
#Advanced programme with exceptions
