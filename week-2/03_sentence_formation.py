# todo: have a list of subjects, verbs and objects. And randomely generate 10 sentences.
import random

def sentence_generator(num):
    subjects = ["Tope", "Anas", "Goke", "Awwal", "Tolu"]
    objects = ["food", "water", "ball", "car", "glass"]
    verbs = ["eats", "kicks", "drinks", "uses", "drives"]
    sentences = set()
    
    for i in range(num):
        single_sentence = f"{random.choice(subjects)} {random.choice(verbs)} {random.choice(objects)}"
        sentences.add(single_sentence)
        if len(sentences) != len(subjects) * len(verbs) * len(objects):
            print(single_sentence)
        else:
            print("There are no more unique random sentences to generate.")
            break
    print(len(sentences))

sentence_generator(1000)
