
number = int(input("Enter a positive integer: "))
if number < 0:
    print("Please enter a positive integer")
elif number == 0:
    print(f'The factorial of {number} is: 1')
else:
    counter = 1
    factorial_number = number
    while counter < number:
        factorial_number *= number-counter
        counter = counter +1
    print(f'The factorial of {number} is: {factorial_number}')