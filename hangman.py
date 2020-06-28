print("Welcome to Hangman!")
print("Press enter to play")
input()
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')


words=[
    "ready",
    "apple",
    "death",
    "Five",
    "app",
    "seattle",
    "salty",
    "nord", 
    "coffee"
]
from random import randint
word = words[randint(0, len(words) - 1)]
print("Guess the word")
print("Ready?")
print (word) 
guess = 7
letters = {}

fail = False
while guess > 0:
    print ("You have", guess, "chances left")
    fail = False
    for c in word:
        if c in letters:
            print(c, end="") 
        else: 
            print("_", end="")
            fail = True
    print ("")
    if not fail:
        print(chr(27)+'[2j')
        print('\033c')
        print('\x1bc') 
        print("Congrates you win the game!")
        print("Hit enter to exit hangman")
        input()
        exit()  

    data = input ()
    guess = guess - 1
    if len(data) == 1:
        letters[data] = True
    else:
        print("That's not a letter")

if fail: 
    print("You've failed")