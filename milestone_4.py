import random as rand

class Hangman():

    def __init__(self, word_list, num_lives = 5):
        self.word = rand.choice(word_list)
        self.word_guessed = ["_"]*len(self.word)
        self.num_letters = len("".join(set(self.word)))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess, word):
        guess = guess.lower()
        word = word.lower()

        if guess in word:
            print(f"Good guess! {guess} is in the word")
            print()

            for i, letter in enumerate(word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters -= 1

        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
            print()

            self.num_lives -=1

            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")

            if not(len(guess) == 1 and guess.isalpha()):
                print("Invalid letter. Please, enter a single alphabetical character.")
                print()
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                print()
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess, self.word)
                
game = Hangman(["Apple", "Banana", "Pineapple", "Grape", "Kiwi"])
print(game.word)
print(game.num_letters)
game.ask_for_input()