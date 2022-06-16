# todo: have a list of subjects, verbs and objects. And randomely generate 10 sentences.
import random

def sentence_generator(num):
    subjects = ["Tope", "Tutor", "Goke", "Awwal", "Tolu", "Faith", "Kunle", "Jide", "Ope", "Gloria"]
    objects = ["house", "hospital", "office", "school", "market"]
    verbs = ["running", "going", "walking", "driving", "crawling"]
    unique = set()

    for i in range(num):
        single_sentence = f"{random.choice(subjects)} is {random.choice(verbs)} to the {random.choice(objects)}"
        unique.add(single_sentence)
    unique_list = list(unique)
    for j in range(len(unique_list)):
        print(unique_list[j])

sentence_generator(int(input("Enter the number of sentence you would like to generate: ")))