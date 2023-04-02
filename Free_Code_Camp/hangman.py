import random
from words import a_word
import string


def get_valid_word(a_word):
    word = random.choice(a_word)     # randomly chooses something from the list 

    while '-' in word or ' ' in word:
        word = random.choices(word)

    return word.upper() 


def hangman():
    word = get_valid_word(a_word)
    word_letter = set(word)       # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # what the user has guessed

    lives = 6


    while len(word_letter) > 0 and lives > 0:

        # getting user input


        print("You have ", lives, "Lives left You have used these letters : ",  ' '.join(used_letters))
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word : ", ''.join(word_list))
        

        user_letter = input("Guess a letter : ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                lives = lives - 1   # takes away a life if wrong
                print("letter is in world.")


        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")


        else:
            print("Invalid character. Please try again.")


    # gets here when len(word_letters) == 0
    if lives == 0:
        print("Sorry, You died. The word was ",word)
        

    print("You guessed the word", word, '!!')




hangman()