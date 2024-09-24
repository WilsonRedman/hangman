def check_guess(guess, word):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            print()

    word = "apple"
    check_guess(guess, word)

ask_for_input()

