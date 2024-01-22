import art
import gamedata

a = art.logo
b = art.vs
c = gamedata.data
print(a)
print('''Welcome to the Higher Lower Game!!!''')
charnum = 1
score = 0
game = True
for character in c:
    while game is True:
        print('Compare the following:')
        print(c[charnum]['name'], 'a ' + c[charnum]['description'] + ' from ' + c[charnum]['country'])
        print(b)
        print(c[charnum + 1]['name'], 'a ' + c[charnum + 1]['description'] + ' from ' + c[charnum + 1]['country'])
        answerlist = [c[charnum]['follower_count'], c[charnum + 1]['follower_count']]
        answer = max(answerlist)
        A = c[charnum]['follower_count']
        B = c[charnum + 1]['follower_count']
        decision = input('Who has more followers? Type "A" or "B":')
        decision.upper()
        if decision == 'A' and answer == A:
            score += 1
            print(f'Correct! Your score is {score}!')
            charnum += 1
            game = True
        elif decision == 'B' and answer == B:
            score += 1
            print(f'Correct! Your score is {score}!')
            charnum += 1
            game = True
        elif decision == 'B' and answer == A:
            print(f'Wrong! Game Over!\n Your score is {score}')
            game = False
        elif decision == 'A' and answer == B:
            print(f'Wrong! Game Over!\n Your score is {score}')
            game = False

#Course Answer(Done on Replit)
from game_data import data
import random
from art import logo, vs
from replit import clear


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()







