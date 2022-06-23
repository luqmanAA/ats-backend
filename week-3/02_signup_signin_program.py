# A signup and sign-in program that take basic info:
# on signup - username, first name, lastname, password and confirm password and saves it in a csv file.
# On signin, it takes username and password and return whether a message saying login successful or invalid
# login credentials.Add validation. Password must be minimum of 8 characters.

import csv

def user():
    action_options = {
        '1': signup,
        '2': signin
    }
    selected_options = input("Welcome, what would you like to do today?\n1. Signup \n2. Sign-in\n")
    if selected_options in action_options:
        return action_options[selected_options]()
    else:
        print("Invalid option, try again")
        return user()

def signup():
    firstname = input("Please enter your firstname: ")
    while firstname == '':
        firstname = input("Firstname cannot be empty, please enter your firstname: ")
    lastname = input("Please enter your last name: ")
    while lastname == '':
        lastname = input("Lastname cannot be empty, please enter your lastname: ")
    username = input("Please enter your username: ")
    while username == '' or len(username) < 6:
        username = input("Username not accepted, username must contain atleast 6 characters: ")
    
    password = input("Enter your password: ")
    while password == '' or len(password) <8:
        password = input("Password must contain at least 8 characters, please try again: ")
    while username.lower() in password.lower() or firstname.lower() in password.lower() or lastname.lower() in password.lower():
        password = input("Unaccepted password! Password cannot contain your username or name, please try again: ")
    
    password_confirm = input("Please confirm your password: ")
    while password_confirm != password:
        password_confirm = input("Those passwords didn't match, please try again: ")
    with open(r'week-3\user_details.csv', 'a') as f:
        headers = ['firstname', 'lastname', 'username', 'password']
        handler = csv.DictWriter(f, fieldnames=headers)
        handler.writerow({
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'password': password
            })
    print("Registration successful")

    
def signin():
    input_username = input("Enter your username to sign-in: ")
    input_password = input("Enter your password: ")
    with open(r'week-3\user_details.csv', 'r') as f:
        handler = csv.DictReader(f)
        for row in handler:
            if (input_username == row['username']) and (input_password == row['password']):
                print("Login Successful!")
            else:
                print("Invalid login credetials, please try again.\n")
                return signin()

user()


