import csv, sys, string, os, pandas as pd

class User:

    file_path = r'week-6\user_profile.csv'
    special_characters = string.punctuation
    headers = ['firstname', 'lastname', 'username', 'password', 'phone_number', 'address', 'dob', 'gender']

    def __init__(self):
       self.file = User.file_path

    def save_data(self, firstname, lastname, username, password):
        with open(self.file, 'a+') as f:
            handler = csv.DictWriter(f, fieldnames=User.headers)
            if os.stat(self.file).st_size == 0:
                handler.writeheader()
            handler.writerow({
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': password
                })
        print("Registration successful! \nPlease signin")
        return self.signin()

    def get_data(self):
        with open(self.file, 'r') as f:
            handler = csv.DictReader(f)
            return (list(handler))

    def validate_username(self, username):
        if len(username) < 6:
            print("Username must contain at least 6 characters")
            return False
        else:
            user_data = self.get_data()
            for data in user_data:
                if username == data['username']:
                    print(f'Username {username} already exist!')
                    return False
            return True
    
    def validate_password(self, password):
        if len(password) < 8:
            print("Unacceptable password! Password must contain 8 characters. Please try again: ", end='')
            return False
        # if (any(i.islower() for i in password) and any(i.isupper() for i in password) and any(i.isnumeric() for i in password) and any(i in self.special_characters for i in password)):
        #     print("Unacceptable password! Password must contain lowercase, uppercase, number and special character. Please try again: ", end='')
        #     return False
        else:
            user_data = self.get_data()
            for data in user_data:
                if data['username'].lower() in password.lower() or data['firstname'].lower() in password.lower() or data['lastname'].lower() in password.lower():
                    print('Unaccepted password! Password cannot contain your username or name, please try again.: ', end='')
                    return False
            return True
    
    def modify_data(self,**kwargs):
        df = pd.read_csv(self.file)
        df_data = self.get_data()
        if len(kwargs) == 2:
            for i in df_data:
                if i['username'] == self.username:
                    df.loc[df_data.index(i), 'password'] = kwargs['password']
            return df.to_csv(self.file, index=False)
        if len(kwargs) > 2:
            for i in df_data:
                if i['username'] == self.username:
                    df.loc[df_data.index(i), 'phone_number'] = kwargs['phone_number']
                    df.loc[df_data.index(i), 'address'] = kwargs['address']
                    df.loc[df_data.index(i), 'dob'] = kwargs['dob']
                    df.loc[df_data.index(i), 'gender'] = kwargs['gender']
            return df.to_csv(self.file, index=False)    
        
    def signin(self):
        username = input("Enter your username to sign-in: ")
        password = input("Enter your password: ")
        # login_data = [username, password]
        user_data = self.get_data()
        for data in user_data:
            if (username == data['username']) and (password == data['password']):
                specific_user_data = data
                print(f'Login Successful!')
                return self.signin_option(**specific_user_data)
            # print(data)
        print("Invalid login credetials, please try again.\n")
        return self.signin()
        # print(user_data)

    def signin_option(self,**kwargs):

        selected_options = input("1. Edit profile \n2. Change password \n3. Logout\n")
        if selected_options == '1':
            return self.edit_profile(kwargs['username'], kwargs['password'])
        elif selected_options == '2':
            return self.change_password(kwargs['firstname'], kwargs['lastname'], kwargs['username'], kwargs['password'])
        elif selected_options == '3':
            sys.exit()
        else:
            print("Invalid option, try again")
            return

    def signup(self):
        firstname = input("Please enter your firstname: ")
        while firstname == '':
            firstname = input("Firstname cannot be empty, please enter your firstname: ")
        lastname = input("Please enter your last name: ")
        while lastname == '':
            lastname = input("Lastname cannot be empty, please enter your lastname: ")
        username = input("Please enter your username: ")
        while not self.validate_username(username):
            username = input("Enter a valid username: ")
        password = input("Enter your password: ")
        while not self.validate_password(password):
            password = input()
    
        password_confirm = input("Please confirm your password: ")
        while password_confirm != password:
            password_confirm = input("Those passwords didn't match, please try again: ")

        user_data = {
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'password': password
                }
        self.save_data(**user_data)

    def change_password(self, firstname, lastname, username, password):
        old_password = input("Enter your old password: ")
        while old_password == '' or old_password != password or len(old_password) <8:
            old_password = input("Password incorrect, please try again: ")
        
        new_password = input("Enter your new password: ")
        while not self.validate_password(password):
            new_password = input("Password must contain at least 8 characters, please try again: ")
        # while username.lower() in new_password.lower() or firstname.lower() in new_password.lower() or lastname.lower() in new_password.lower():
        while username.lower() in new_password.lower() or firstname.lower() in new_password.lower() or lastname.lower() in new_password.lower():
            new_password = input("Unaccepted password! Password cannot contain your username or name, please try again: ")
        
        new_password_confirm = input("Please confirm your new password: ")
        while new_password_confirm != new_password:
            new_password_confirm = input()

        self.modify_data(**{'username': username, 'password': new_password})
        
        print("Password succesfully changed")
        return

    def edit_profile(self, username, password):
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
        self.modify_data(**user_info)
        print("Profile updated successfully!")
        return