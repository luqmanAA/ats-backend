import random,  string
from prime_number_check import prime_check

letters = string.ascii_letters
eratosthenes_list = [random.choice(letters) for i in range(1000)]


for i in range(2, len(eratosthenes_list)):
    if prime_check(i):
        eratosthenes_list[i] = 1
    else:
        eratosthenes_list[i] = 0

prime_subscript = []

for i in range(len(eratosthenes_list)):
    if eratosthenes_list[i] == 1:
        prime_subscript.append(i)

# print(prime_subscript)
print(eratosthenes_list)
