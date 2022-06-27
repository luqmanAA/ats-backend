def prime_check(num:int):
    if num == 2 or num == 3:
        return True
    sq_root = int(num**0.5)
    for i in range(2, sq_root+1):
        if num % i == 0:
            return False
    return True


prime_list = [i for i in range(2,1001) if prime_check(i)]

# print(prime_list)
