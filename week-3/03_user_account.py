# A signup and sign-in program that take basic info:
# on signup - username, first name, lastname, password and confirm password and saves it in a csv file.
# On signin, it takes username and password and return whether a message saying login successful or invalid
# login credentials.Add validation. Password must be minimum of 8 characters.

##### Modifications
# 1. After successful signup, it should prompt the user to signin.
# 2. After successful signin, user should be presented with the options: Edit profile, Change password, Logout.
# 3. Edit profile should ask for more information like phone_number (required), address (optional), date of birth (optional) and gender (compulsory)

import csv
import sys

headers = ['firstname', 'lastname', 'username', 'password', 'phone_number', 'address', 'dob', 'gender']

def save_data(firstname, lastname, username, password):
    with open(r'week-3\user_accounts.csv', 'a+') as f:
        handler = csv.DictWriter(f, fieldnames=headers)
        # handler.writeheader()
        handler.writerow({
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'password': password
            })
    print("Registration successful! \nPlease signin")
    return signin()

def retrieve_data():
    # print(username, password)
    with open(r'week-3\user_accounts.csv', 'r') as f:
        handler = csv.DictReader(f)
        return (list(handler))

def modify_data(**kwargs):
    data_holder = []
    with open(r'week-3\user_accounts.csv', 'r+') as f:
        data_reader = csv.DictReader(f, fieldnames=headers)
        for data in data_reader:
            if len(kwargs) == 2:
                if (kwargs['username'] == data['username']):
                    data['password'] = kwargs['password']
            if len(kwargs) > 2:
                if (kwargs['username'] == data['username']):
                    data['password'] = kwargs['password']
                    data['phone_number'] = kwargs['phone_number']
                    data['address'] = kwargs['address']
                    data['dob'] = kwargs['dob']
                    data['gender'] = kwargs['gender']
            data_holder.append(data)
    with open(r'week-3\user_accounts.csv', 'w') as f:
        data_writer = csv.DictWriter(f, fieldnames=headers)
        # data_writer.writeheader()
        for data in data_holder:
            data_writer.writerow(data)

def signin():
    username = input("Enter your username to sign-in: ")
    password = input("Enter your password: ")
    # login_data = [username, password]
    user_data = retrieve_data()
    for data in user_data:
        if (username == data['username']) and (password == data['password']):
            specific_user_data = data
            print(f'Login Successful!')
            return signin_option(**specific_user_data)
        # print(data)
    print("Invalid login credetials, please try again.\n")
    return signin()
    # print(user_data)

def signin_option(**kwargs):

    selected_options = input("1. Edit profile \n2. Change password \n3. Logout\n")
    if selected_options == '1':
        return edit_profile(kwargs['username'], kwargs['password'])
    elif selected_options == '2':
        return change_password(kwargs['firstname'], kwargs['lastname'], kwargs['username'], kwargs['password'])
    elif selected_options == '3':
        sys.exit()
    else:
        print("Invalid option, try again")
        return user()

def signup():
    user_data = retrieve_data()
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

    user_data = {
            'firstname': firstname,
            'lastname': lastname,
            'username': username,
            'password': password
            }
    save_data(**user_data)


def change_password(firstname, lastname, username, password):
    old_password = input("Enter your old password: ")
    while old_password == '' or old_password != password or len(old_password) <8:
        old_password = input("Password incorrect, please try again: ")
    
    new_password = input("Enter your new password: ")
    while new_password == '' or len(new_password) <8:
        new_password = input("Password must contain at least 8 characters, please try again: ")
    # while username.lower() in new_password.lower() or firstname.lower() in new_password.lower() or lastname.lower() in new_password.lower():
    while username.lower() in new_password.lower() or firstname.lower() in new_password.lower() or lastname.lower() in new_password.lower():
        new_password = input("Unaccepted password! Password cannot contain your username or name, please try again: ")
    
    new_password_confirm = input("Please confirm your new password: ")
    while new_password_confirm != new_password:
        new_password_confirm = input("Those passwords didn't match, please try again: ")

    modify_data(**{'username': username, 'password': new_password})
    
    print("Password succesfully changed")
    return signin_option()
            

def edit_profile(username, password):
    phone_number = input("Please enter your phone number (required): ")
    while phone_number == '' or not phone_number.isnumeric() or len(phone_number) < 11:
        phone_number = input("Phone number is required, please enter your phone number: ")
    address = input("Please enter your address: ")
    dob = input("Please enter your date of birth: ")
    gender = input("Please enter your gender (m/f): ")
    while gender == '' or not gender.isalpha() or not (gender == 'm' or gender == 'f'):
        gender = input("Invalid gender, please enter your gender: ")
    user_info = {
        'username': username,
        'password': password,
        'phone_number': phone_number,
        'address': address,
        'gender': gender,
        'dob': dob
    }
    modify_data(**user_info)
    print("Profile updated successfully!")
    return signin_option()


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

user()