#Leap Year identifier
#This is how you work out whether if a particular year is a leap year.
#on every year that is divisible by 4 with no remainder
#except every year that is evenly divisible by 100 with no remainder
#unless the year is also divisible by 400 with no remainder

year = int(input('Enter a year:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'Year {year} is a leap year')
else:
    print(f'Year {year} is not a leap year')

#Output, given the year 2002
#Enter a year:2002
#Year 2002 is not a leap year



# Course answer
year = int(input())

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")