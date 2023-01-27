import random
import string
from wordds import wordds


def get_valid_word(wordds):
    word = random.choice(wordds)  #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(wordds)

    return word.upper()


def hangman():
    word = get_valid_word(wordds)
    word_letters = set(word)  #letters that are already guessed
    alphabet = set(string.ascii_uppercase) #all alphabets in capital
    used_letters = set()  #what the user has

    lives = 10

    #getting user input
    while len(word_letters) > 0 and lives > 0:
        #letters used
        print("You have", lives, "lives left and you have used these letters:", ' '.join(used_letters))  #.join makes a A B C kinda of the letters

        #what current word is (ie W-RD)
        word_list = [letter if letter in used_letters else '-' for letter in word] #telling if the letter is in the word by checking guess put that letter in word_list else put a dash -
        print("Current word:", ' '.join(word_list))

        user_letter = input("Enter a letter:").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 #takes away a life if wrong answer

        elif user_letter in used_letters:
            print("You just guessed that letter")

        else:
            print("Invalid character")

    if lives == 0:
        print("You have died. sorry. The word was", word)
    else:
        print("You have guessed the correct word congratulations!", word)


hangman()