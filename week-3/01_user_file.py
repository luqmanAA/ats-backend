#A program that asks for your username, first name, last name, password, password confirmatuon and saves it in a text file with name as username

username = input("Enter your username: ")
firstname = input("Enter your first name: ")
lastname = input("Enter yuour last name: ")
password = input("Enter your password: ")
password_confirm = input("Confirm your password: ")
file_path =f"week-3\\{username}.txt"
if password == password_confirm:
    with open(file_path, "w") as f:
        f.write(f"Firstname: {firstname} \nLastname: {lastname} \nUsername: {username}\nPassword: {password}")
else:
    print("Those passwords didn't match")