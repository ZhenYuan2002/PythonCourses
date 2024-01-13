##Calculate how many tons of paint you need to paint a wall
#1 can of paint can cover 5 square meters of a wall
#Given: random height, random width
#calculate how many tons of paint you need to buy
#My take
import math
def paint_calc(height, width, cover):
    number_of_cans = (height * width)/coverage
    number_of_cans = math.ceil(number_of_cans)
    print('You will need ' + str(number_of_cans) + ' cans of paint')



test_h = int(input()) #height of wall
test_w = int(input()) # width of wall
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)