# asterisks_list = list('*'*10)


# for asterisk in asterisks_list:
#     pattern_asterisk += asterisk
#     print(f'{pattern_asterisk}')

print("A")
for i in range(10):
    print('*'*i)



print("\nB")
for i in reversed(range(10)):
    print('*'*i)


print("\nC")
length = 10
for n in range(length):
    blanks = " " * n
    stars = "*" * (length - n)
    print(f"{blanks}{stars}")

print("\nD")
length = 10
for n in range(length):
    blanks = " " * n
    stars = "*" * (length - n)
    print(f"{blanks}{stars}")