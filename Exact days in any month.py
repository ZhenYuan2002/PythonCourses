def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not Leap Year")





# TODO: Add more code here 👇
# MY TAKE



#Use variable is_leap to check the inputs: Year and Month
#Output the number of days in the month
#if its a leap year and if its febraury, there are 29 day instead of 28
def days_in_month(fyear, fmonth):
    month_days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(fyear) == print('Not Leap Year'):
        return f'There are {month_days[fmonth - 1]} days in year {fyear}'
    elif is_leap(fyear) == print('Leap Year'):
        if fmonth == 1:
            return f'There are 29 days in year {fyear}'
        elif fmonth != 1:
            return f'There are {month_days[fmonth - 1]} days in year {fyear}'
#The output answer, although correct, also types out either 'Leap Year' or 'Not Leap Year' 2 times

#COURSE ANSWER
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]







# 🚨 Do NOT change any of the code below
year = int(input())  # Enter a year
month = int(input())  # Enter a month
days = days_in_month(fyear = year, fmonth = month)
print(days)
