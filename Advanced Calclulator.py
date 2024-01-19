#!!!!!!!!UPDATE
#Code now no longer works in python, as function when returned is sotred in memory



#MY TAKE

#Add
def add(n1, n2):
    return float(n1 + n2)

#Subtract
def subtract(n1, n2):
    return float(n1 - n2)

#Divide
def divide(n1, n2):
    return float(n1 / n2)

#Multiply
def multiply(n1, n2):
    return float(n1 * n2)


operations = {
    "+" : add,
    "-" : subtract,
    "/" : divide,
    "*" : multiply
}
print(operations)

num1 = int(input('Whats the first number?'))
num2 = int(input('Whats the second number?'))

for symbol in operations.keys():
    print(symbol, end = ' ')

operation_symbol = input('\nChoose a symbol from the line above')
if operation_symbol == '+':
    answer = add
elif operation_symbol == '-':
    answer = subtract
elif operation_symbol == '/':
    answer = divide
elif operation_symbol == '*':
    answer = multiply

#calculator_function = operations[operation_symbol]
#calculator_function(num1, num2)

print(f'{num1} {operation_symbol} {num2} = {answer}')


#Course Answer
#Done on replit
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
