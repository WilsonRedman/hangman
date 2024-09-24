import random as rand

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask__for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = rand.choice(word_list).lower()
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len("".join(set(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

        print(f"The mystery word has {self.num_letters} characters")

    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        
        guess = guess.lower()
        word = self.word

        if guess in word:
            print(f"Good guess! {guess} is in the word\n")

            for i, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.\n")

            self.num_lives -=1

            print(f"You have {self.num_lives} lives left.\n")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_guess method.
        '''

        while True:
            print(self.word_guessed)
            guess = input("Guess a letter: ")

            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.\n")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!\n")
            else:
                break
        self.list_of_guesses.append(guess)
        self.check_guess(guess)

def play_game(word_list):

    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print(f"You lost! The wors was {game.word}")
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
