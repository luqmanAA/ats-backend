import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''']

def get_words_list():
    with open(r'week-3\words.txt', 'r') as file:
        list_of_words = file.readlines()
        return(list_of_words)


def get_random_word():
    return((random.choice(get_words_list())).strip())

def fill_gap():
    random_word = get_random_word()
    gap = '_'*len(random_word)
    print(gap)
    for i in range(0, 8):
        guess_letters = input(f"Guess a letter in the word (you have {8 - i} guesses left): ").lower()
        letter_check = ''
        while len(guess_letters) > 1:
            guess_letters = input(f"Guess just one letter in the word (you have {8 - i} guesses left): ").lower()
            print(stages[7-i])
        for j in range (0, len(random_word)):
            if random_word[j] == guess_letters:
                gap = gap[:j] + random_word[j] + gap[j+1:]
        
        letter_check += guess_letters
        if letter_check not in gap:
            print("Your guess is wrong!")
        print(gap)
        if '_' not in gap:
            break
    if '_' not in gap:
        print(f"Weldone! You guessed the word correctly after {i+1} guesses")
    else:
        print("You lost! You've exhausted your number of guesses!")
        
fill_gap()
# print(stages[7])
