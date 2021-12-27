import words
import random
import string


def get_a_valid_world(liste):
    word = random.choice(liste)
    while " " in word or "-" in word:
        word = random.choice(liste)
    return word


print(get_a_valid_world(words.liste))
# print(len(words))


def hangman():
    word = get_a_valid_world(words.liste)
    words_letters = set(word)
    alphabet_letters = set(string.ascii_uppercase)
    used_letters = set()


# getting the user input

# user_input = input("Gess a letter:").upper()
# if user_input in alphabet_letters - used_letters:
