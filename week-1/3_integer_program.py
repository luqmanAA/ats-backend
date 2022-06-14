#Programs that gets an integer then determines if it's greater, less or equal to zero

integer_number = int(input("Enter an integer"))

if integer_number > 0:
    print(f"{integer_number} is greater than 0")
elif integer_number == 0:
    print(f"{integer_number} is equals to 0")
else:
    print(f"{integer_number} is less than 0")
