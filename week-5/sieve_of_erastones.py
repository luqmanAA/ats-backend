
# list_of_numbers = [1]*1000

# for number in range(len(list_of_numbers)):

#     if number == 0 or number == 1:
#         list_of_numbers[number] = 0
    
#     elif number == 2 or number == 3:
#         continue
#     else:
#         for num in range(2,number):
#             if number % num == 0:
#                 list_of_numbers[number] = 0

# # print(list_of_numbers)


# prime_numbers = []

# def prime_check(num):
#     if num == 0 or num == 1:
#         return False
    
#     elif num == 2 or num == 3:
#         return True
#     else:
#         for i in range(2,num):
#             if num % i == 0:
#                 return False
#         return True

# for number in range (len(list_of_numbers)):
#     if not prime_check(number):
#         list_of_numbers[number] = 0
#     elif prime_check(number):
#         prime_numbers.append(number)

# print(list_of_numbers)
# print(prime_numbers)


import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    mil_hour = 0
    if s[-2:].lower() == "pm" and s[:2] != "12":
        mil_hour = 12 + int(s[:2])
    print(mil_hour, s[-2:].lower())
    if  mil_hour > 12 and mil_hour < 24:
        return(f"{str(mil_hour)}{s[2:-2]}")
    elif s[:2] == 12 or mil_hour == 24:
        return("00" + s[2:-2])
    else:
        return(s[0:-2])
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
