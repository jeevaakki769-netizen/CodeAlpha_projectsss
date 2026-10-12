
import random

# List of 5 predefined words
words = ["python", "computer", "apple", "coding", "program"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to the Hangman Game!")
print("Guess the word one letter at a time.")

while incorrect_guesses < max_incorrect_guesses:
    # Display guessed and hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:",
          max_incorrect_guesses - incorrect_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word!")
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! The word was:", secret_word)
