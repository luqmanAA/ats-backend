
import sys

def calculator():
    def multiply(num1, num2):
        return f"Result is: {num1*num2}"

    def add(num1, num2):
        return f"Result is: {num1+num2}"

    def subtract(num1, num2):
        return f"Result is: {num1-num2}"

    def divide(num1, num2):
        try:
            print(f"Result is: {num1/num2}")
        except ZeroDivisionError:
            print("invalid divisor")


    operand1 = int(input("Enter your first operand: "))
    operator = input("Enter the operation you'd like to perform (e.g + - / *): ")
    operand2 = int(input("Enter your second operand: "))

    if operator == '*':
        print(multiply(operand1, operand2))
    elif operator == '+':
        print(add(operand1, operand2))
    elif operator == '-':
        print(subtract(operand1, operand2))
    elif operator == '/':
        divide(operand1, operand2)
    else:
        print("That is not a valid operator")

    another_operation= input("WOuld you like to perform another operation (Y/N)? ")

    if another_operation.lower() == 'y':
        calculator()
    elif another_operation.lower() == 'n':
        print("Thank you, see you next time!")
    else:
        print("Invalid input")
    
    sys.exit

calculator()