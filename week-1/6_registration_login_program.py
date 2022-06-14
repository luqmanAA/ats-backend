### Program that takes user info, saves it then asks user to login

firstname = input("Welcome, enter your first name? ")
lastname = input ("Enter your last name? ")
username = input ("What username would you like to use? ")
password = input("Enter your preffered password. Please take note of your password.: ")

print("Well done, your registration was successful!")

login_username = input("Enter your username: ")

if login_username != username:
    print("Sorry, we do not know a user with that username!")
else:
     login_password = input("Enter your password: ")
     if login_password == password:
         print(f"Welcome {firstname}, you logged in successfully!")
     else:
         print("You entered a wrong password, please try again")