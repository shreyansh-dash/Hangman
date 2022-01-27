import random
from words import Words
import string
from hangman_visual import lives_visual_dict

def get_valid_words(words): 
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_words(Words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters) > 0  and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])

        user_letter = input('Guess a letter: ').upper()

    user_letter = input('Guess a letter of your choice').upper()  # just to maintain uniformity
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)
            print('')
        else:
            lives = lives-1 
            print('\n Your letters,', user_letter, 'is not in the word.')
    elif user_letter in used_letters:
        print('\n You have already used that letter. Guess another please')
    else:
        print('\nThat is not a valid letter.')

    # when live and len are == 0

    if lives == 0:
        print(lives_visual_dict[lives])
        print('You dies, sorry. The word was', word)

    else:
        print('YAY! You gussed the word', word, '!!!!')



if __name__ == '__main__':
    hangman()