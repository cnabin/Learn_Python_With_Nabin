# Calculator Prtogram   
#  Requirements
# Ask the user for two numbers
# Ask the user which arithmentic operation does he/she wnats to perform on those two numbers
# Perform the operation and print the result in terminal

num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

operator=input("Enter the operation you want to perform (+,-,*,/): ")

if operator=='+':
    result1=num1+num2
    print(f"\n The addition of {num1} and {num2} is {result1}")

elif operator=='-':
    print(f"The subtraction of {num1} and {num2} is {num1-num2}")

elif operator=='*':
    print(f"The multiplication of {num1} and {num2} is {num1*num2}")

elif operator=='/':
    print(f"The division of {num1} and {num2} is {int(num1/num2)}")

else:
    print("The assigned operator is not available")

user_choice=input("Do you want to perform further operation with the resulted value (Yes/No):")

if user_choice=='Yes':
    number1=int(input("Enter the number you want to operate with resultant value: "))
    print(f"The resultant value after assigned second value is {result1+number1}")

else:
    print("Till now available for + operation after Yes confirmation")
