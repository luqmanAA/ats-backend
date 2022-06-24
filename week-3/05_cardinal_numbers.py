def number_to_word(n:int):
    unique_numbers = {
    0: 'th',1: "st", 2: "nd", 3: "rd", 4: "th",5: "th",6: "th", 7: "th",8: "th",9: "th"
    }
    unit = n % 10
    tens = n % 100
    if tens == 11 or tens == 12 or tens == 13:
        return str(n)+'th'
    return str(n)+unique_numbers[unit]

print(number_to_word(10013))