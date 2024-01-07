#BMI Calculator
#Tells you your BMI value rounded off to 2.d.p as well as your weight category


height = float(input('Enter your height in meters\n'))
weight = int(input('Enter your weight in kg\n'))
heightsquared = height * height
BMIwithoutrounding = weight/heightsquared
BMI = round(BMIwithoutrounding,2)

#In the following nested if statements there are different string formats used
if BMI < 18.5:
    print('Your BMI is ' + str(BMI) + ' which puts you in the underweight category')
if BMI >= 18.5 and BMI < 25:
    print(f'Your BMI is {BMI}, which is in the normal weight range')
if BMI >= 25 and BMI <30:
    print('Your BMI is {}, which puts you in the slightly overweight category'.format(BMI))
if BMI >= 30 and BMI < 35:
    print(f'Your BMI is {BMI}, which puts you in the obese category')
if BMI >=35:
    print(f'Your BMI is {BMI}, which puts you in the clinically obese category')

#Example Output, given that a person's height is 1.75 and weight is 82KG:
Enter your height in meters
1.78
Enter your weight in kg
82
Your BMI is 25.88, which puts you in the slightly overweight category


#Alternatively, there are also elif and else statements used to save memory space
height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
