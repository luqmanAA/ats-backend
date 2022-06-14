import string

def encode (data: list):
    digits = string.digits
    special_char = string.punctuation
    alpha_lower = string.ascii_lowercase
    alpha_upper = string.ascii_uppercase
    rev_alpha_lower = alpha_lower[::-1]
    vowels = ['a', 'e', 'o', 'i', 'u']
    vowels_map = ['#', '$', '%', '&', '*']
    enc = []

    for s in data:
        if s.lower() in vowels:
            enc.append(vowels_map[vowels.index(s.lower())])
        elif s == '|':
            enc.append(data[data.index(s)+1])
            data.remove(s)
        elif s == '^':
            t = data[data.index(s)+1]
            enc.append(digits[rev_alpha_lower.index(t)])
            data.remove(s)
        elif s in vowels_map:
            enc.append(vowels[vowels_map.index(s)])
        elif s in special_char:
            enc.append('|'+s)
        elif s in alpha_lower + alpha_upper:
            enc.append(s.swapcase())
        elif s in digits:
            enc.append('^'+ rev_alpha_lower[digits.index(s)])
        # else:
        #     enc.append(" ")
    
    return ("".join(enc))

print(encode(list(input("Enter the text to encode or decode: "))))
