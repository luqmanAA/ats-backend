import string

letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
letters_list = []
first_ten_letters = []
last_ten_letters = []
vowels = []
consonants = []
vowels_list = []
consonants_list = []

for i in letters:
    letters_list.append(i)

for i in range(10):
    first_ten_letters.append(letters_list[i])

for i in range(1,11):
    last_ten_letters.append(letters_list[-i])

for i in letters:
    if i in 'aeiou':
        vowels.append(i)
    continue

for i in letters:
    if i in 'aeiou':
        continue
    consonants.append(i)

print(first_ten_letters)
print(last_ten_letters)
print(vowels)
print(consonants)


#2 English alphabets separated with comma
for i in vowels:
    vowels_list.append(i)

for i in consonants:
    consonants_list.append(i)

vowels_consonants = vowels_list + consonants_list
vowels_consonants.sort()
comma_strings = ",".join(vowels_consonants)

print(comma_strings)


3 

def word_checker(word):

    if word.isupper():
        print(word,"is uppercase")
    elif word.islower():
        print(word,"is lowercase")
    else:
        print(word,"is mixed case")

# word_checker(input("Enter the word to check: "))


#4. Gets a dictionary and returns the keys and values

# def key_value (data):
#     word_list = data.split(',')
#     new_dic = {}
#     new_dic[word_list[0]]= word_list[1]
#     keys = new_dic.keys()
#     values = new_dic.values()

#     print(keys, "is the key and ", values, "is the value")

# key_value(input("Enter two values separated by ',': "))

#5.
numbers = [1,2,3,4,5]

for i in range(6,11):
    numbers.append(i)

print(numbers)