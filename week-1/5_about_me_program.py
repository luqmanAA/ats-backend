###Program that asks for personal info and writes an essay on it

from email import message


name = input("What is your name?: ").lower()
town = input("Which town are you from?: ").lower()
state = input("And your state is?: ").lower()
education = input("What is your level of education? Type 'SSCE', 'Bachelors' or 'Masters': ").lower()
employement = input("What is your employement status? Type 'Student', 'Self Employed', 'Employed' or 'Unemployed': ").lower()
interest = input("What is that one thing you do when you're not working? e.g reading, traveling, gaming etc: ").lower()
likes = input("What is your like?: ").lower()
dislikes = input("And your dislike?: ").lower()
special_quote = input("What quote represents your philosophy?: ").lower()
favorite_food = input("What is that food that will get you happy like a kid?: ")
favorite_color = input("What is your favorite color: ")

message = f"####################### \nMy name is {name}, a native of {town} in {state} state. "
if education == "":
    message = message
elif education == "ssce":
    message += "I am a School cert holder. "
elif education == "bachelors":
    message += "I am a Bachelor's degree holder. "
elif education == "master":
    message += "I am a Masters degree holder. "
else:
    message+= "I don't have a formal education. "

if education == "":
    message = message
elif employement == "student":
    message += "I am still an undergraduate.\n"
elif employement == "self employed":
    message += "I am an enterprenuer.\n"
elif employement == "employed":
    message += "I am gainfully employed.\n"
elif employement == "unemployed":
    message += "I am seriously looking for job, help my life!\n"
else:
    message+= "I just dey, dey enjoy.\n"

if interest == "":
    message = message
else:
    message += f"I love {interest}. "

if likes == "":
    message = message
else:
    message += f"I like {likes} "

if dislikes == "":
    message = message
else:
    message += f"and I hate {dislikes}. "

if special_quote == "":
    message = message
else:
    message += f"A philosophy I live by is '{special_quote}'.\n"

if favorite_food == "":
    message = message
else:
    message += f"I can follow you wherever you want if you give me {favorite_food}. Infact, {favorite_food} is to me as Caprisome is to kids. "

if interest == "":
    message+= "I don't think I have a favorite color. I go with any color. \n #######################"
else:
    message += f"If there's only one color in the world, you found me wearing {favorite_color}. \n #######################"


print(message)