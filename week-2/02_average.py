# function that takes five numbers and compute the average

def average_of_numbers(num1, num2, num3, num4, num5):
    sum = num1 + num2 + num3 + num4 + num5
    average = sum/5
    return average

# print(average_of_numbers(5,10,15,20,25))

#function that takes 5 arguments and print the type of each

def type_of_data(a:int, b:str, c:dict, d:list, e:tuple):
    print(f"{a} is {type(a)}")
    print(f"{b} is {type(b)}")
    print(f"{c} is {type(c)}")
    print(f"{d} is {type(d)}")
    print(f"{e} is {type(e)}")

number = 465
letters = "aeiou"
value_list = ["ade", "bolu", 245]
value_dict = {
    "age": 15,
    "name": "Ade"
}
value_tuple = ("a", "b", "c", 4, 5)

# type_of_data(number, letters, value_list, value_dict, value_tuple)

#Factor