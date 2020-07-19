from random import randint
from readchar import readkey
from readchar.key import CTRL_C


def clear():
    print("\x1bc")

clear()
print("Welcome to Hangman!")
print("Press enter to play")
readkey()

clear()

words=[
    "ready",
    "apple",
    "death",
    "five",
    "app",
    "seattle",
    "salty",
    "nord", 
    "coffee"
]

word = words[randint(0, len(words) - 1)]
print("Guess the word\nReady?")

guess = 7
letters = {}

fail = False
while guess > 0:
    print ("You have", guess , "chances left")
    fail = False
    for c in word:
        if c in letters:
            print(c, end="") 
        else: 
            print("_", end="")
            fail = True

    print("")
    if not fail:
        clear()
        print("Congrates you win the game! The word was", word)
        print("Hit enter to exit hangman")
        readkey()
        exit()  

    data = readkey()
    if data == CTRL_C:
        exit(0)

    if data in letters:
        print("Already guessed that letter.")
        guess = guess - 1

    letters[data] = True

    if data not in word:
        guess = guess - 1

if fail:
    clear()
    print("You've failed :(")
    print("The word was", word + ".")
