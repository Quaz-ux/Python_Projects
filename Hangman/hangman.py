import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.replace("-", " ").upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used letters:', ' '.join(used_letters))
        # current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word is:', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:


                lives -= 1
                print("Letter is not in the word.")
        elif user_letter in used_letters:
            print('You already used that character. Please type other character.')
        else:
            print('Invalid character {}. Please type other character.'.format(user_letter))

    if lives == 0:
        print('You died sorry. The word was:', word)
    else:
        print('You have guessed the word:', word)

hangman()
