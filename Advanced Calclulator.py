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