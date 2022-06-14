from operator import index


numbers_list = [1,2,3,4,5]
numbers_tuples = (1,2,3,4,5)
numbers_string = "12345"
numbers_set = {1,2,3,4,5}
numbers_dict = {1: 1, 2: "word", 3: 3, 4: 4, 'a': 'a'}

# for number in numbers_dict:
#     print(number)

# numbers_dict + {"d": 4}
# print(numbers_dict)

# i = 0
# while i<len(numbers_list):
#     print(numbers_list[i])
#     i = i + 1

numbers = [1,2,3,4,5,6,7,8,9,10]

for number in numbers:
    if number % 2 == 0:
        print (number)

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print (numbers[i])
    i = i +1