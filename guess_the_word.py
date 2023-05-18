import random

def play_game():
    words = ["apple", "banana", "cherry", "durian", "elderberry"]
    word = random.choice(words)
    guessed_letters = []
    turns = 12

    while turns > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        print("Guessed word:", guessed_word)
        print("Turns left:", turns)

        if guessed_word == word:
            print("Congratulations! You guessed the word correctly!")
            return

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            turns -= 1
            print("Wrong guess!")

    print("Sorry, you lost. The word was", word)

play_game()
