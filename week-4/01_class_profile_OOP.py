from datetime import date


list_of_profiles = {
    "labisoye@afexnigeria.com": {"firstname" : "Lukman", "lastname" : "Abisoye", "dmob": "16-10", "attendance": 10, "height": 175, "weight": 62, "age": 23},
    "aadeleke@afexnigeria.com": {"firstname" : "Awwal", "lastname" : "Adeleke", "dmob": "20-05", "attendance": 11, "height": 190, "weight": 70, "age": 23},
    "aadeyeye@afexnigeria.com": {"firstname" : "Adebusola", "lastname" : "Adeyeye","dmob": "10-04", "attendance": 10, "height": 178, "weight": 55, "age": 21},
    "yoyedele@afexnigeria.com": {"firstname" : "Yusuff", "lastname" : "Oyedele", "dmob": "14-08", "attendance": 9, "height": 180, "weight": 63, "age": 26},
    "bbalogun@afexnigeria.com": {"firstname" : "Basheer", "lastname" : "Balogun", "dmob": "16-07", "attendance": 10, "height": 180, "weight": 60, "age": 25},
    "asalaam@afexnigeria.com": {"firstname" : "Abdullahi", "lastname" : "Salaam", "dmob": "02-01", "attendance": 11, "height": 172, "weight": 68, "age": 25},
    "aadekunle@afexnigeria.com":{"firstname" : "Abraham", "lastname" : "Adekunle", "dmob": "25-03", "attendance": 11, "height": 183, "weight": 65, "age": 23},
    "atajudeen@afexnigeria.com": {"firstname" : "Abdulwali", "lastname" : "Tajudeen", "dmob": "16-07", "attendance": 11, "height": 193, "weight": 75, "age": 20},
    "fadeosun@afexnigeria.com": {"firstname" : "Faith", "lastname" : "Adeosun", "dmob": "05-05", "attendance": 7, "height": 168, "weight": 61, "age": 23},
    "asharafudeen@afexnigeria.com": {"firstname" : "Ahmad", "lastname" : "Sharafudeen", "dmob": "12-02", "attendance": 11, "height": 178, "weight": 61, "age": 24},
    "togunbiyi@afexnigeria.com": {"firstname" : "Toluwanimi", "lastname" : "Ogunbiyi", "dmob": "09-12", "attendance": 9, "height": 188, "weight": 81, "age": 24}
}

class Profile:
    def __init__(self, **kwargs):
        self.data = kwargs
        self.birth_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.current_year = date.today().year

    def update_attendance(self, email):
        if email.lower() in self.data:
            self.data[email]['attendance'] += 1
            return(f"{self.data[email]['firstname']}'s new attendance is {self.data[email]['attendance']}")
        return (f'No student exist with email: {email}')
    
    def update_name(self, email):
        new_firstname = input("Enter the new first name: ")
        new_lastname = input("Enter the new last name: ")
        
        if email.lower() in self.data:
            self.data[email]['firstname'] = new_firstname
            self.data[email]['lastname'] = new_lastname
            return(f"New first name is {self.data[email]['firstname']} and new lastname is {self.data[email]['lastname']}")
        return (f'No student exist with email: {email}')
    
    def get_fullname(self, email):
        if email.lower() in self.data:
            fullname = f"{self.data[email]['firstname']} {self.data[email]['lastname']}"
            return(f"The full name is {fullname.title()}")
        return (f'No student exist with email: {email}')

    def get_number_of_students(self):
        return len(self.data)
    
    def add_student(self):
        new_profile_email = input("Enter the email address of the new student: ")
        new_profile = {}
        new_profile.update({"first_name": input("Enter the firstname of the new profile: ")})
        new_profile.update({"last_name": input("Enter the lastname of the new profile: ")})
        new_profile.update({"date": input("Enter the brith date and month of the new profile e.g 05-07: ")})
        new_profile.update({"attendance": int(input("Enter the attendance for the new profile: "))})
        new_profile.update({"height": int(input("Enter the height of the new profile: "))})
        new_profile.update({"weight": int(input("Enter the weight of the new profile: "))})
        new_profile.update({"age": int(input("Enter the age of the new profile: "))})

        self.data.update({new_profile_email: new_profile})
        return self.data

    def remove_student(self,email):
        if email.lower() in self.data:
            print(f"Number of students before removal is: {len(self.data)}")
            self.data.pop(email)
            return(f"Number of students after removal is: {len(self.data)}")
        return (f'No student exist with email: {email}')
    
    def get_birth_month(self,email):
        if email.lower() in self.data:
            month = int(self.data[email]['dmob'][-2:])
            birth_month = self.birth_months[month-1]
            return(f"{self.data[email]['firstname']}'s birth month is: {birth_month}")
        return (f'No student exist with email: {email}')

    def group_by_birth_month(self):
        same_month = []        
        for i in range(len(self.birth_months)):
            for j in self.data:
                if i+1 == int( self.data[j]['dmob'][-2:]):
                    name = f"{self.data[j]['firstname']} {self.data[j]['lastname']}"
                    same_month.append(name)
            if same_month != []:
                print(f"Students born in {self.birth_months[i]}: {' and '.join(same_month)}")
            same_month.clear()
    
    def get_students_initials(self):
        list_of_initials = []
        for i in self.data:
            initials = self.data[i]["firstname"][0] +'.'+self.data[i]["lastname"][0]
            list_of_initials.append(initials)
        return(list_of_initials)
    
    def get_BMI(self,email):
        if email.lower() in self.data:
            height_in_meters = self.data[email]["height"]/100
            bmi = self.data[email]["weight"]/(height_in_meters**2)
            return(f"{self.data[email]['firstname']}'s BMI is: {round(bmi,2)}")
        return (f'No student exist with email: {email}')
    
    def get_average_age(self):
        sum = 0
        for i in self.data:
            sum += self.data[i]["age"]
        average = sum/len(self.data)
        return(f"The average age of the class is :{round(average, 2)}")
    
    def get_minimum_age(self):
        min = 30
        for i in self.data:
            if self.data[i]["age"] < min:
                min = self.data[i]["age"]
        return(f"The minimum age in the class is: {min}")

    def get_maximum_age(self):
        max = 0
        for i in self.data:
            if self.data[i]["age"] > max:
                max = self.data[i]["age"]
        return(f"The maximum age in the class is: {max}")

    def get_birth_year(self, email):
        if email.lower() in self.data:
            birth_year = self.current_year - self.data[email]["age"]
            return(f"The birth year for {self.data[email]['firstname']} is: {birth_year}")
        return (f'No student exist with email: {email}')

student = Profile(**list_of_profiles)

# print(student.update_attendance('togunbiy@afexnigeria.com'))
# print(student.update_name('labisoye@afexnigeria.com'))
# print(student.get_number_of_students())
# print(student.remove_profile('labisoye@afexnigeria.com'))
# print(student.add_student())
# print(student.get_birth_month('aadeleke@afexnigeria.com'))
# print(student.get_students_initials())
# print(student.get_BMI('labisoye@afexnigeria.com'))
# print(student.get_average_age())
# print(student.get_minimum_age())
# print(student.get_maximum_age())
# print(student.get_birth_year('labisoye@afexnigeria.com'))
student.group_by_birth_month()