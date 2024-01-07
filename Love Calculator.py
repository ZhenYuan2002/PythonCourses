print("The Love Calculator is calculating your score...")
name1 = input('Enter Player 1 name\n')
name2 = input('Enter Player 2 name\n')

name1l = name1.lower()
name2l = name2.lower()
name1true = int(name1l.count('t')) + int(name1l.count('r')) + int(name1l.count('u')) + int(name1l.count('e'))
name2true = int(name2l.count('t')) + int(name2l.count('r')) + int(name2l.count('u')) + int(name2l.count('e'))
trueoccourance = int(name1true) + int(name2true)
name1love = int(name1l.count('l')) + int(name1l.count('o')) + int(name1l.count('v')) + int(name1l.count('e'))
name2love = int(name2l.count('l')) + int(name2l.count('o')) + int(name2l.count('v')) + int(name2l.count('e'))
loveoccourance = int(name1love) + int(name2love)
scores = str(trueoccourance) + str(loveoccourance)
score = int(scores)
if score < 10 or score > 90 :
    print('Both of you go together like coke and chicken!')
if score >= 40 and score <= 50 :
    print(f'Your score is {score}, yall are alright together')
else:
    print(f'Your score is {score}')