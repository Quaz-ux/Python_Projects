import random
import string

from words import words


def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0:
        print('You have used letters: ', ' '.join(used_letters))
        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is: ', ' '.join(word_list))
        user_letter = input('Guess a letter: ').upper()
        if user_letter is alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You already used that character. Please type other character.')

        else:
            print(f'Invalid character {user_letter}. Please type other character.')


user_input = input('Type something: ')
hangman()
