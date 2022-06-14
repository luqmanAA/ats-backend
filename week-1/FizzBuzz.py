# ##Fizz - Buzz program

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)

import string


letters = "aBDEWKAsklaouehsjAJSAW"
upper =""
lower=""


for i in letters:
    if ord(i) >= 65 and ord(i) <= 90:
        upper += i
    else:
        lower += i

print (len(upper))