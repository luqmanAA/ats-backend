#Census program that stores firstname, lastname, middle name, age, gender, dob, occupation, marital status,email
#validates input
#saves in a csv file
#Ability to search by taking a search term and return matches

import csv
from datetime import date

def census():
    action_options = {
        '1': add_profile,
        '2': search_profile
    }
    selected_options = input("Welcome to Nigeria Population Commisiona portal, what would you like to do today?\n1. Add new profile \n2. Search for profile\n")
    if selected_options in action_options:
        return action_options[selected_options]()
    else:
        print("Invalid option, try again")
        return census()

def add_profile():
    current_year = date.today().year
    firstname = input("Welcome to Nigeria Population Commisiona portal, \nPlease enter your firstname: ")
    while firstname == '':
        firstname = input("Firstname cannot be empty, please enter your firstname: ")
    lastname = input("Please enter your last name: ")
    while lastname == '':
        lastname = input("Lastname cannot be empty, please enter your firstname: ")
    middlename = input("Please enter your middle name: ")
    email = input("Please enter your email address: ")
    while '@' not in email:
        email = input("Please enter a valid email address")
    age = input("Please enter your age: ")
    while not age.isnumeric():
        age = input("Please enter your age in number: ")
    gender = input("Please enter your gender (m/f): ")
    while gender == '' or not gender.isalpha() or not (gender == 'm' or gender == 'f'):
        gender = input("Invalid gender, please enter your gender: ")
    dob = input("Please enter your date of birth (e.g dd-mm-yyyy): ")
    while dob == '':
        dob = input("Date of birth cannot be empty, please enter your date of birth: ")
    # year_of_birth = dob.split('-')
    # calculated_age = current_year - int(year_of_birth[-1])
    # while calculated_age < int(age) or calculated_age > int(age):
    #     dob = input("Please enter a date of birth with valid year: ")
    marital_status = input("Please enter your marital status: ")
    occupation = input("Please enter your Occupation: ")

    with open(r'week-3\census.csv', 'w') as f:
        headers = ['firstname', 'lastname', 'middlename', 'email', 'age', 'gender', 'dob', 'marital_status', 'occupation']
        handler = csv.DictWriter(f, fieldnames=headers)
        handler.writeheader()
        handler.writerow({
            'firstname': firstname,
            'lastname': lastname,
            'middlename': middlename,
            'email':email,
            'age':age,
            'gender':gender,
            'dob':dob,
            'marital_status':marital_status,
            'occupation':occupation})
def search_profile():
    search_term = input('Enter what you would like to search with: ')
    with open(r'week-3\census.csv', 'r') as f:
        handler = csv.DictReader(f)
        for row in handler:
            if (search_term.lower() in row['firstname'].lower()) or (search_term.lower() in row['lastname'].lower()) or (search_term.lower() in row['middlename'].lower()) or (search_term.lower() in row['email'].lower()):
                print(row)
            else:
                print("No user with such term, try again")
                return search_profile()

census()