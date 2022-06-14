import numbers
from re import X


num_count = int(input("Enter the number of element you want in the list: "))
numbers_list = []
max = 0
for i in range(num_count):
    numbers_list.append(int(input("Enter the element: ")))

for i in numbers_list:
    if i > max:
        max = i

print(max, "is greater")