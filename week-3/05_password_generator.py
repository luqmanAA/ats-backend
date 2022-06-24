import string, random

lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
characters = string.punctuation

def password_generator():
    password = []
    for i in range(4):
        password.append(random.choice(lower))
        password.append(random.choice(upper))
        password.append(random.choice(numbers))
        password.append(random.choice(characters))
    random.shuffle(password)
    return password

# print(f"Your generated password is: {''.join(password_generator())}")

def username_generator(firstname, lastname):
    username = []
    username.append(firstname[0] + lastname)
    username.append(lastname[0] + firstname)
    username.append(lastname+firstname)
    for i in range(3):
        username.append(username[i][::-1])

    return(random.choice(username))

print(username_generator('lukman', 'adewale'))