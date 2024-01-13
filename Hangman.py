#Step 3
import random
word_list = ['aardvark', 'baboon', 'camel']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print('Psst, the solution is ' + chosen_word)
display = []
for _ in range(word_length):
    display += "_"

#Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the
#choosen word and 'display' has no more blanks ("_"). Then you can tell the user that they have won
guess = input("Guess a letter: ").lower()

guesses_left = 6
while guesses_left > 0:
    if '_' in display:
        for position in range(word_length):
            letter = chosen_word[position]
            print(f'Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}')
            if letter == guess:
                display[position] = letter
                print(display)
                guesses_left -= 1
                guess = input(f"You have {guesses_left} gussess left!\nGuess a letter: ").lower()
    elif '_' not in display:
        print('Congratulations! You guessed the word!')
        break

else:
    print('Sorry, you ran out of guesses')































