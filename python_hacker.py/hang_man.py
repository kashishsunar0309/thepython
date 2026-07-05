import random

print("Welcome to Hangman!")

words = ["hacker", "bounty", "random"]
secret_word = random.choice(words)
print(secret_word)
print("You have only 5 chance.")


# create display with underscores using a loop
display_word = []
for letter in secret_word:
    display_word.append("_")

print(display_word)


num = 0
game_over = False

while not game_over:
    guess = input("Guess a letter: ").lower()

    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f" You have {guesses_left}guesses_left")
        if num >= 5:
            print("You lost ---😒")
            game_over = True
    print(display_word)

    if "_" not in display_word:
        print("You Win 🤘---")
        game_over = True
