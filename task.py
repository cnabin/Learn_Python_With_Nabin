# Requirements
# During input chech if the input is number or not
# If it is a number then convert it into float and do the calculation
# But if it is not a number ask the user for the number again
# isdigit


number1 = float(input('Enter a number : ')) # Error
number2 = float(input('Enter another number : '))

operator = input('Enter the operation you want to perform(+,-,*,/):')

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
else:
    print('The operator you provided is not available!')

# Requirements
# During input check if the input is number or not
# If it is a number then convert it into float and do the calculation
# But if it is not a number ask the user for the number again until the user provides a number