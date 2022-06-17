unique_numbers = {
    "0": "", "1": "One", "2": "Two","3": "Three","4": "Four","5": "Five","6": "Six","7": "Seven","8": "Eight","9": "Nine","10": "Ten",
    "11": "Eleven","12": "Twelve","13": "Thirteen","14": "Fourteen","15": "Fifteen","16": "Sixteen","17": "Seventeen","18": "Eighteen","19": "Nineteen","20": "Twenty",
    "30": "Thrity","40": "Forty","50": "Fifty","60": "Sixty","70": "Seventy","80": "Eighty","90": "Ninety"
}

def number_to_words(number):
    values_of_units = ""
    values_of_tens = ""
    values_of_hundreds = ""
    values_of_thousand = ""

    if len(number) == 4:
        values_of_thousand += number[-4]
        values_of_hundreds += number[-3]
        values_of_tens += number[-2]
        values_of_units += number[-1]
    elif len(number) == 3:
        values_of_hundreds += number[-3]
        values_of_tens += number[-2]
        values_of_units += number[-1]
    elif len(number) == 2:
        values_of_tens += number[-2]
        values_of_units += number[-1]

    integer_of_tens_values = 0

    if number in unique_numbers or int(number) <= 20:
        return(unique_numbers[number])
    elif int(number) > 20 and len(number) == 2:
        return (f"{unique_numbers[values_of_tens +'0']} {unique_numbers[values_of_units]}")

    elif int(number) > 99 and len(number) == 3:
        if values_of_tens == "0" and values_of_units == "0":
            hundreds = f"{unique_numbers[values_of_hundreds]} hundred"

        elif values_of_tens == "0" or values_of_tens == "1":
            integer_of_tens_values += int(values_of_tens + values_of_units)
            hundreds = f"{unique_numbers[values_of_hundreds]} hundred and {unique_numbers[str(integer_of_tens_values)]}"

        else:
            hundreds = f"{unique_numbers[values_of_hundreds]} hundred and {unique_numbers[values_of_tens+'0']} {unique_numbers[values_of_units]}"
        return(hundreds)

    elif int(number) > 999 and len(number) == 4:
        if values_of_hundreds == "0" and values_of_tens == "0" and values_of_units == "0":
            thousands = f"{unique_numbers[values_of_thousand]} thousand"

        elif not (values_of_hundreds == "0") and values_of_tens == "0" and values_of_units == "0":
            thousands = f"{unique_numbers[values_of_thousand]} thousand, {unique_numbers[values_of_hundreds]} hundred"

        elif values_of_hundreds == "0" and (values_of_tens == "0" or values_of_tens == "1"):
            integer_of_tens_values += int(values_of_tens + values_of_units)
            thousands = f"{unique_numbers[values_of_thousand]} thousand and {unique_numbers[str(integer_of_tens_values)]}"

        elif int(values_of_hundreds) >= 1 and int(values_of_tens) == 1:
            thousands = f"{unique_numbers[values_of_thousand]} thousand, {unique_numbers[values_of_hundreds]} hundred and {unique_numbers[values_of_tens+values_of_units]}" 
        
        else:
            thousands = f"{unique_numbers[values_of_thousand]} thousand, {unique_numbers[values_of_hundreds]} hundred and {unique_numbers[values_of_tens+'0']} {unique_numbers[values_of_units]}"
        return(thousands)


print(number_to_words(input("Enter the number: ")))
