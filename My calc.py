# Setup Variables
first = int(input('Num1 = '))
num = int(input('Num2 = '))

print('Choose x for Multiplication')
print('Choose / for Division')
print('Choose + for Addition')
print('Choose - for Subtraction')

# Get operation input
operation = input('Choose operation (x, /, +, -): ')

# Perform operation
if operation == 'x' or operation == 'X':
    result = first * num
elif operation == '/':
    if num == 0:
        print("Error: Cannot divide by zero.")
        result = None
    else:
        result = first / num
elif operation == '+':
    result = first + num
elif operation == '-':
    result = first - num
else:
    result = None
    print('Error! Invalid operation.')

if result is not None:
    print('Result:', result)

# Ask to continue
i = input('Continue? (yes or no): ')

if i.lower() == 'yes' and result is not None:
    next_op = input('Choose next operation (x, /, +, -): ')
    b = int(input('Num3 = '))
    
    if next_op == 'x' or next_op == 'X':
        print('Result:', result * b)
    elif next_op == '/':
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            print('Result:', result / b)
    elif next_op == '+':
        print('Result:', result + b)
    elif next_op == '-':
        print('Result:', result - b)
    else:
        print('Error! Invalid operation.')
