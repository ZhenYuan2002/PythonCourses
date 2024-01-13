#Prime numbers are numbers that can only be clearly divided by themselves and 1
#Write a function that checks whether if the number passed into it is a prime number or not

def prime_checker(number):
    if number % 2 == 0 and number != 2:
        print(f'{number} is not a prime number')
    elif number % 3 == 0 and number != 3:
        print(f'{number} is not a prime number')
    elif number % 4 == 0 and number != 4:
        print(f'{number} is not a prime number')
    elif number % 5 == 0 and number != 5:
        print(f'{number} is not a prime number')
    elif number % 6 == 0 and number != 6:
        print(f'{number} is not a prime number')
    elif number % 7 == 0 and number != 7:
        print(f'{number} is not a prime number')
    elif number % 8 == 0 and number != 8:
        print(f'{number} is not a prime number')
    elif number % 9 == 0 and number != 9:
        print(f'{number} is not a prime number')
    elif number % 10 == 0 and number != 10:
        print(f'{number} is not a prime number')
    else:
        print(f'{number} is a prime number')

n = int(input())
prime_checker(number=n)