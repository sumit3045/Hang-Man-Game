import random
from words import words
import string
def get_valid_words(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()

def hang_man():
    word=get_valid_words(words)
    lives=6


    alphabet=set(string.ascii_uppercase)#taking all alhpabets
    word_letters=set(word)#seperating the letters of the selected random word
    used_letters=set()#making a list of the used words


    while len(word_letters)>0 and lives>0:
        print("You have ",lives,"lives and have used the following letters: ",' '.join(used_letters))
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print("The current word: ",' '.join(word_list))


        user_input=input("Enter a letter you think is right: ").upper()
        if user_input in alphabet-used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                lives=lives-1
        elif user_input in used_letters:
            print("You have already used this letter!")
        else:
            print("Invalid input")
    if lives==0:
        print(f"You lost! The correct word was {word}")
    else:
        print(f'YES! You have gussed the word {word} correctly!')

hang_man()









