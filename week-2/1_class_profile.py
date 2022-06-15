list_of_profiles = [
    {"first_name" : "Lukman", "last_name" : "Abisoye", "date": {"day": 16, "month": "October"}, "attendance": 10, "height": 175, "weight": 62, "age": 23},
    {"first_name" : "Awwal", "last_name" : "Adeleke", "date": {"day": 20, "month": "May"}, "attendance": 11, "height": 190, "weight": 70, "age": 23},
    {"first_name" : "Adebusola", "last_name" : "Adeyeye", "date": {"day": 10, "month": "April"}, "attendance": 10, "height": 178, "weight": 55, "age": 21},
    {"first_name" : "Yusuff", "last_name" : "Oyedele", "date": {"day": 14, "month": "August"}, "attendance": 9, "height": 180, "weight": 63, "age": 26},
    {"first_name" : "Basheer", "last_name" : "Balogun", "date": {"day": 16, "month": "July"}, "attendance": 10, "height": 180, "weight": 60, "age": 25},
    {"first_name" : "Abdullahi", "last_name" : "Salaam", "date": {"day": 2, "month": "January"}, "attendance": 11, "height": 172, "weight": 68, "age": 25},
    {"first_name" : "Abraham", "last_name" : "Adekunle", "date": {"day": 25, "month": "March"}, "attendance": 11, "height": 183, "weight": 65, "age": 23},
    {"first_name" : "Abdulwali", "last_name" : "Tajudeen", "date": {"day": 16, "month": "July"}, "attendance": 11, "height": 193, "weight": 75, "age": 20},
    {"first_name" : "Faith", "last_name" : "Adeosun", "date": {"day": 5, "month": "May"}, "attendance": 7, "height": 168, "weight": 61, "age": 23},
    {"first_name" : "Ahmad", "last_name" : "Sharafudeen", "date": {"day": 12, "month": "February"}, "attendance": 11, "height": 178, "weight": 61, "age": 24},
    {"first_name" : "Toluwanimi", "last_name" : "Ogunbiyi", "date": {"day": 9, "month": "December"}, "attendance": 9, "height": 188, "weight": 81, "age": 24}
]

months_of_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


#1 function that increments profile attendance

def attendance_update(class_profile,name):
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            i["attendance"] = i["attendance"] + 1
            return(f"{name}'s new attendance is {i['attendance']}")

print(attendance_update(list_of_profiles, input("Enter the name of the user whose attendance you'd like to increment: ")))

#2
def name_update(class_profile, name):
    new_first_name = input("Enter the new first name: ")
    new_last_name = input("Enter the new last name: ")
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            i["first_name"] = new_first_name
            i["last_name"] = new_last_name
    return(f"New first name is {new_first_name} and new lastname is {new_last_name}")

# print(name_update(list_of_profiles,input("Enter the first name of the account: ")))

#3
def full_name(class_profile,name):
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            fullname = i["first_name"] + " " + i["last_name"]
    return(f"The full name is {fullname.title()}")

# print(list_of_profiles,full_name(input("Enter the first name of the account: ")))

#4
def add_profile(class_profile):
    new_profile = {}
    new_profile.update({"first_name": input("Enter the firstname of the new profile: ")})
    new_profile.update({"last_name": input("Enter the lastname of the new profile: ")})
    new_profile.update({"date": dict(zip(["day", "month"], input("Enter the date and month of the new profile e.g 10 January: ").split()))})
    new_profile.update({"attendance": int(input("Enter the attendance for the new profile: "))})
    new_profile.update({"height": int(input("Enter the height of the new profile: "))})
    new_profile.update({"weight": int(input("Enter the weight of the new profile: "))})
    new_profile.update({"age": int(input("Enter the age of the new profile: "))})

    class_profile.append(new_profile)
    return class_profile

# print(add_profile(list_of_profiles))


#5
def number_of_people(class_profile):
    return(len(class_profile))

# print(number_of_people(class_profile))

#6
def remove_profile(class_profile,name):
    print(f"Number of users before removal is: {len(class_profile)}")
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            class_profile.remove(i)
            break
    return(f"Number of users after removal is: {len(class_profile)}")

# print(remove_profile(list_of_profiles,input("Enter the first name of the profile you'd like to remove: ")))

#7
def birth_month(class_profile,name):
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            return(f"{name}'s birth month is: {i['date']['month']}")


# print(birth_month(list_of_profiles,input("Enter the first name of the user whose birth month you'd like to know: ")))

#8 - Group by birth month
def month_group(profiles):
    grouped_by_month = {}
   
    for profile in profiles:
        # grouped_by_month = {profile:[k for k in months_of_year if files[k] == n] for n in set(files.values())}
        
        # for month in months_of_year:
            
        if profile["date"]["month"]  in months_of_year:
            same_month = []
            same_month.append(profile["first_name"]+ " "+profile["last_name"])
            grouped_by_month.update({profile["date"]["month"]: same_month})
        
    return(grouped_by_month)

print(month_group(list_of_profiles))

#9
def initials_list(class_profile):
    list_of_initials = []
    
    for i in class_profile:
        initials = i["first_name"][0] +'.'+i["last_name"][0]
        list_of_initials.append(initials)
    return(list_of_initials)

# print(initials_list(list_of_profiles))

#10
def profile_BMI(class_profile,name):   
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            height_in_meters = i["height"]/100
            bmi = i["weight"]/(height_in_meters**2)
            return(f"The BMI of {name} is: {round(bmi,2)}")

# print(profile_BMI(list_of_profiles,input("Enter the first name of the user whose BMI you'd like to know: ")))

#11
def age_stats(class_profile):
    sum = 0
    max = 0
    min = class_profile[0]["age"]
    for i in class_profile:
        sum += i["age"]
        if i["age"] > max:
            max = i["age"]
        if i["age"] < min:
            min = i["age"]
    
    average = sum/len(class_profile)
    print(f"The average age of the class is :{int(average)}")
    # print(f"The minimum age in the class is: {min}")
    # print(f"The maximum age in the class is: {max}")
    return [int(average), min, max]


# print(age_stats(list_of_profiles))

#12 Calculate birth year
def birth_year(class_profile,name):
    for i in class_profile:
        if i["first_name"].lower() == name.lower():
            birth_year = 2022 - i["age"]
            return(f"The birth year for {name} is: {birth_year}")


# print(birth_year(list_of_profiles,input("Enter the first name of the user whose birth year you'd like to know: ")))


###Description of the class
class_age = age_stats(list_of_profiles)
description = f'''The class has {number_of_people(list_of_profiles)} students. The oldest student in the class is {class_age[2]} 
years old and the youngest is {class_age[1]} years old and it has an average age of {class_age[0]}.'''

print(description)