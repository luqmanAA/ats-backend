from random import randint
import string

vowels = ['a', 'e', 'i', 'o', 'u']
lower_letters = list (string.ascii_lowercase)
special_char = ["#", '$', '%', '&', '*']
random_char = string.punctuation
encoded_txt = ""


characters = input("Enter the text you would like to encode: ")


for i in characters:
    if i.isdecimal():
        j = int(i)
        encoded_txt += str(lower_letters[-(j+1)])
    elif i in random_char:
        encoded_txt += '|'+ i
    # elif i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
    elif i in vowels:
        #for key in vowels:
        encoded_txt += special_char[vowels.index(i)]
    else:
        encoded_txt += i.swapcase()

print(f"{characters} is encoded as {encoded_txt}")

    