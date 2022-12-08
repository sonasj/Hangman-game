import random
import string
def main():
    global tries
name = input("====================WELCOME TO HANGMAN GAME!=====================\n Please enter your name: ")
print("HELLO, ",name.upper())
hardwords = ['voodoo','horse','vortex','teapot','nature','outside','spring','circus''wave','zombie','zipper','youthful','wheezy','yatchtsman','wellspring','zigzagging','yippee','waltz']
simpwords = ['jazz','buzz','fuzz','zit','fox','puff','fit','deep','frog','shallow','cat','bird','star','book','apple','nose']
score = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
gamemode = input("CHOOSE A LEVEL - EASY(6 guesses) or HARD(11 guesses)\n").upper()
if(gamemode == 'EASY'):
    tries = 11
    words = random.choice(simpwords)
else:
    tries = 7
    words = random.choice(hardwords)
print(gamemode) 
def lives_visual_dict2(tries):
    HARDHANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    return HARDHANGMANPICS[tries] 

words2 = ['jazz','buzz','fuzz','zit','fox','puff','fit','deep','frog','shallow','cat','bird','star','book','apple','nose']
def get_valid_word(words2):
    word = random.choice(words2)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words2)

    return word.upper()


def EASYhangman(): 
    
    word = get_valid_word(words2)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 11
    score = 0
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict(lives-1))
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
                score = score + 2

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict(lives))
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
    print("score",score) 



def lives_visual_dict(tries):
    EASYHANGMANPICS = ['''
     +---+
     |   |
         |
         |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
         |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
     |   |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
   //|   |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
   //|\  |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
   //|\\\ |
         |
         |
   =========''', '''
     +---+
     |   |
     O   |
   //|\\\ |
    /    |  
         |
   =========''','''
     +---+
     |   |
     O   |
   //|\\\ |
    / \  |
         |
   =========''','''
     +---+
     |   |
     O   |
   //|\\\ |
   //    |
         |
   =========''','''
     +---+
     |   |
     O   |
   //|\\\ |
   // \  |
         |
   =========''','''
     +---+
     |   |
     O   |
   //|\\\ |
   // \\\ |
         |
   =========''']
    return EASYHANGMANPICS[tries]










words =  ['voodoo','horse','vortex','teapot','nature','outside','spring','circus''wave','zombie','zipper','youthful','wheezy','yatchtsman','wellspring','zigzagging','yippee','waltz']

def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()




def HARDhangman(): 
    
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    lives = 7
    score = 0
    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict2(lives-1))
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
                score = score + 2

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict2(lives-1))
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
    print("score",score)










if __name__ == '__main__':
    if(gamemode == 'EASY'):
        EASYhangman()
    else:
        HARDhangman()
    
playagain = input("IF YOU WANT TO PLAY AGAIN WITH SAME GAMEMODE.PRESS Y.OTHERWISE N\n").upper()
if(playagain =='Y'):
   if __name__ == '__main__':
    if(gamemode == 'EASY'):
        EASYhangman()
    else:
        HARDhangman()
    
else:
    exit