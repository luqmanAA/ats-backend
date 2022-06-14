def perfect_number(num):
    sum = 0
    for i in range(1, num+1):
        if num % i == 0:
            sum += i
    if (2*num) == sum:
        print(num, "is a perfect number")
    else:
        print(num, "is not a perfect number")

perfect_number(int(input("Enter a number: ")))

