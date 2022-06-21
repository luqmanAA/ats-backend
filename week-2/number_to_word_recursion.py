def number_to_word(n:int):
    unique_numbers = {
    1: "One", 2: "Two", 3: "Three", 4: "Four",5: "Five",6: "Six", 7: "Seven",8: "Eight",9: "Nine",10: "Ten",
    11: "Eleven",12: "Twelve",13: "Thirteen",14: "Fourteen",15: "Fifteen",16: "Sixteen",17: "Seventeen",18: "Eighteen",19: "Nineteen",20: "Twenty",
    30: "Thrity",40: "Forty",50: "Fifty",60: "Sixty",70: "Seventy",80: "Eighty",90: "Ninety", 100: "One hundred"
    }
    unit = n % 10
    tens = ((n % 100) // 10)*10
    hundreds = (n % 1000) // 100
    thousands = n // 1000
    
    if n in unique_numbers:
        return unique_numbers[n]

    elif n > 20 and n <=99:
        return(f"{unique_numbers[tens]}-{unique_numbers[unit]}")

    elif n < 999 and n % 100 == 0:
        return(f"{unique_numbers[hundreds]} hundred")

    elif (n < 999) or (n < 999 and n %100 < 20):
        return(f"{unique_numbers[hundreds]} hundred and {number_to_word(n%100)}")

    elif n > 999 and n % 1000 == 0:
        return(f"{unique_numbers[thousands]} thousand")

    elif n > 999:
        return(f"{unique_numbers[thousands]} thousand, {number_to_word(n % 1000)}")


print(number_to_word(int(input("Enter the number: "))))