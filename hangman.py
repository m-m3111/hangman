import random
from words import words
import string

def get_valid_words(words):
    word= random.choice(words)
    while ' ' in words or '_' in word:
        word= random.choice(words)
    return word    

def hangman():
    word = get_valid_words(words)
    letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used = set()

    while (len(letters) > 0):
        print('you have used these letters: ' + ' '.join(used))
        word_list = [l if l in used else '-' for l in word]
        print('current word: ' + ' '.join(word_list))

        user_letter = input('guess a letter')
        if user_letter in alphabet - used:
            used.add(user_letter)
            if user_letter in letters:
                letters.remove(user_letter)

        elif user_letter in used:
            print("you've already guessed it")

        else:
            print('invalid character')    

hangman()