from cardinal_number import cardinal

read_input = []
for i in range(20):
    user_input = int((input(f"Enter the {cardinal(i+1)} number: ")))
    while user_input in read_input:
        user_input = int((input(f"Number already exist, enter another one: ")))
    read_input.append(user_input)
    print(user_input)

print(read_input)
