import random as rand

word_list = ["Apple", "Banana", "Pineapple", "Grape", "Kiwi"]
print(word_list)

word = rand.choice(word_list)
print(word)

guess = input("Enter a single Letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")