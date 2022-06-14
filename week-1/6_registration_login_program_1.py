### This program checks your login credentials

username = "admin"
password = "password"

login_username = input("Enter your username: ")

if login_username != username:
    print("Sorry, we do not know a user with that username!")
else:
     login_password = input("Enter your password: ")
     if login_password == password:
         print("Welcome, you logged in successfully!")
     else:
         print("You entered a wrong password, please try again")