e = 1
count = 1

def number_factorial(number):
    counter = 1
    factorial_number = number
    while counter < number:
        factorial_number *= number-counter
        counter = counter +1
    return(factorial_number)

while count <= 10:
    e += 1/number_factorial(count)
    count = count + 1
print(f'The evaluation of the mathematical constant (e) is: {e}')