#Course Outline:
#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs.
#Then check for the number of times the letters in the word LOVE occurs.
#Then combine these numbers to make a 2 digit number.

#For Love Scores less than 10 or greater than 90, the message should be:
#"Your score is *x*, you go together like coke and mentos."
#For Love Scores between 40 and 50, the message should be:
#"Your score is *y*, you are alright together."
#Otherwise, the message will just be their score. e.g.:
#"Your score is *z*."


#Example Outputs
#Name 1	        Name 2	            Score
#Brad Pitt	    Jennifer Aniston	73
#Prince William	Kate Middleton	    67
#Ashton Kutcher	Mila Kunis	        63
#David Beckham	Victoria Beckham	45
#Mario	        Princess Peach	    43
#Kanye West	    Kim Kardashian	    42


#My solution
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
    print('Both of you go together like coke and mentos!')
if score >= 40 and score <= 50 :
    print(f'Your score is {score}, yall are alright together')
else:
    print(f'Your score is {score}')



#Course solution
print("The Love Calculator is calculating your score...")
name1 = input()  # What is your name?
name2 = input()  # What is their name?
# Your code below this line 👇
combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")

