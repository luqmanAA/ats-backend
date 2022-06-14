
import string

letters = input("Enter a sentence to check: ")

upper_letters = string.ascii_uppercase
lower_letters = string.ascii_lowercase

alpha_lower = ""
alpha_upper = ""

for i in letters:
    if i in lower_letters:
        alpha_lower += i
    elif i in upper_letters:
        alpha_upper += i

num_of_lower = len(alpha_lower)
num_of_upper = len(alpha_upper)

print(f"The sentence has {num_of_upper} letters in uppercase and {num_of_lower} letters in lowercase ")
