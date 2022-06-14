import string


def pangram (letters):
    lower_letters = set(string.ascii_lowercase)
    new_letters = ""
    for i in letters:
        if i == " ":
            new_letters += letters[letters.index(i)+1]
        else:
            new_letters += i.lower()
    
    set_of_letters = set(new_letters)

    if set_of_letters == lower_letters:
        print("The sentence  is a pangram")
    else:
        print("The sentence is not a pangram")

pangram(input("Enter a sentence: "))