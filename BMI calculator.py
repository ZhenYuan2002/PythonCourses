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
    print('Your BMI is {} which puts you in the slightly overweight category'.format(BMI))
if BMI >= 30 and BMI < 35:
    print(f'Your BMI is {BMI}, which puts you in the obese category')
if BMI >=35:
    print(f'Your BMI is {BMI}, which puts you in the clinically obese category')

#Example Output, given that the person's height is 1.75 and weight is 82KG