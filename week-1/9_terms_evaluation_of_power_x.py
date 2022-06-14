e = 1
count = 1
x = int(input("Enter the value of x: "))
def number_factorial(number):
    counter = 1
    factorial_number = number
    while counter < number:
        factorial_number *= number-counter
        counter = counter +1
    return(factorial_number)

while count <= 10:
    e += (x**count)/number_factorial(count)
    count = count + 1
print(f'The evaluation of the value of e^x is: {e}')