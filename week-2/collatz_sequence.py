def collatz(n):
    if n % 2 == 0:
        print(n // 2)
        return n // 2
    if n % 2 == 1:
        print(3 * n + 1)
        return 3 * n + 1

try:
    number = int(input("Enter a number: "))
    while number > 1:
        number = collatz(number)
except ValueError:
    print("Enter a valid integer")