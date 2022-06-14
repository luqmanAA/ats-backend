#Program that gets a gender and returns its pronoun

gender = input("Welcome, please enter your gender\n").lower()

if gender == "male":
    print("It is a He")
elif gender == "female":
    print ("It is a she")
else:
    print("You do not exist!")