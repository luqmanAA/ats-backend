from random import randint
import string

# vowels = ['a', 'e', 'i', 'o', 'u']
vowels = {
    "a":'#',
    "e":'$',
    "i":'%',
    "o":'&',
    "u":'*'
}
# lower_letters = string.ascii_lowercase
consonants = "bcdfghjklmnpqrstvwxyz"
special_char = string.punctuation
encoded_txt = ""


characters = input("Enter the text you would like to encode: ")


for i in characters:
    if i.isdecimal():
        j = int(i)
        encoded_txt += str(consonants[-(j+1)])
    elif i in special_char:
        encoded_txt += '|'+ i
    # elif i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
    elif i in consonants:
        #for key in vowels:
        encoded_txt += i.swapcase()
        # encoded_txt += special_char[randint(0, len(special_char)-1)]
    else:
        for key, value in vowels:
            y = 
        encoded_txt += vowels[i]

print(f"{characters} is encoded as {encoded_txt}")

    