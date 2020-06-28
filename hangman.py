print("Welcome to Hangman!")

words=[
    "ready",
    "apple",
    "death",
    "apple",
    "apple"
]
from random import randint
word = words[randint(0, len(words) - 1)]
print (word)
guess = 5
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
        print("C0NgRaTeS yOu WiN")  

    data = input ()
    guess = guess - 1
    if len(data) == 1:
        letters[data] = True
    else:
        print("That's not a letter")

if fail: 
    print("You've failed")