import random


number = random.randint(1,10)
print(number)
num = input("Guess a number between 1 and 10: ")

def number_guess(num):
    # i = 4
    # while num != number and i > 0:
    #     num = input("Try again: ")
    #     i -= 1
    for i in range(5):
        if int(num) == number:
            print("Great! You guessed the right number")
            break
    print(f"You failed! Correct number is {number}")

#     return num
    
# if int (num) != number:
#     new_num = number_guess(num)
#     if new_num!= number:
#         print(f"You failed! Correct number is {number}")
    
# else:
#     print("Great! You guessed the right number")

number_guess(num)