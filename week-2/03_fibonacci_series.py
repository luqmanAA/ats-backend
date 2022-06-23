def fib(n):
    numbers = []
    for i in range (n):
        if i == 0 or i == 1:
            numbers.append(i)
        else:
            numbers.append(numbers[i-1] + numbers[i-2])
    print(numbers)


#fib(10)

def fib_rec(n):
    if n == 0 or n == 1:
        return n
    return (fib_rec(n-1) + fib_rec(n-2))

print(fib_rec(40))