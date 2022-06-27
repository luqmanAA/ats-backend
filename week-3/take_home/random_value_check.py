import random


dict_random_values = {
    'key_1': random.randrange(1,99), 'key_2': random.randrange(1,99),
    'key_3': random.randrange(1,99), 'key_4': random.randrange(1,99),
    'key_5': random.randrange(1,99), 'key_6': random.randrange(1,99),
    'key_7': random.randrange(1,99), 'key_8': random.randrange(1,99),
    'key_9': random.randrange(1,99), 'key_10': random.randrange(1,99),
    'key_11': random.randrange(1,99), 'key_12': random.randrange(1,99),
    'key_13': random.randrange(1,99), 'key_14': random.randrange(1,99),
    'key_15': random.randrange(1,99), 'key_16': random.randrange(1,99),
    'key_17': random.randrange(1,99), 'key_18': random.randrange(1,99),
    'key_19': random.randrange(1,99), 'key_20': random.randrange(1,99),
}

list_of_values = []

for k, v in dict_random_values.items():
    list_of_values.append(v)

list_of_values.sort()

if len(list_of_values) > len(set(list_of_values)):
    print(f"There are {len(list_of_values) - len(set(list_of_values))} duplicate values")
else:
    print("No duplicate values")

# print(list_of_values)
# print(set(list_of_values))