#!/usr/bin/env python3

word = input('Please enter a word for your opponent: ')

# Initialize variables
wrongGuesses = 7
guessed = False
correctLetters = ''
wrongLetters = ''
blanks = ''

for letter in word:
    blanks = blanks+'_ '

print(blanks)

print('You have', wrongGuesses, 'wrong guesses left.')

while guessed is False and wrongGuesses > 0:

    print('Correct Letters Guessed: ', correctLetters)
    print('Wrong Letters Guessed: ', wrongLetters)

    guess = input('What letter would you like to guess?')

    blanks = ''
    validLetter = False

    for letter in word:
        if letter == guess:
            validLetter = True

    if validLetter == True:
        correctLetters = correctLetters + guess
        print('Correct!', 'The letter', guess, 'is in the word.')
    else:
        wrongLetters = wrongLetters + guess
        wrongGuesses = wrongGuesses - 1
        print("I'm sorry,", guess, "is not in the word.")
        print('You have', wrongGuesses, 'wrong guesses left.')