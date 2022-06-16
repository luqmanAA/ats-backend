num1 = int(input("Enter the value of a: "))
num2 = int(input("Enter the value of b: "))
num3 = int(input("Enter the value of c: "))

def quadratic_calculator(a,b,c):
    product_of_a_c = a * c
    factors=[number for number in range(-abs(product_of_a_c), abs(product_of_a_c) + 1) if number != 0 and product_of_a_c % number == 0]
    
    middle_term = [factor for factor in factors for i in range(len(factors)) if factor + factors[i] == b and factor * factors[i] == product_of_a_c]
    
    if len(middle_term) == 0:
        print("That equation cannot be solved by factorization method")
    elif a >= 1 and len(middle_term) == 1:
        print(f"values of x are {-middle_term[0]} and {-middle_term[0]}")
    elif a == 1:
        print(f"values of x are {(-middle_term[0])} and {-middle_term[1]}")
    elif a > 1 or a < 0:
        print(f"values of x are {(-middle_term[0])/a} and {(-middle_term[1])/a}")

quadratic_calculator(num1,num2,num3)
