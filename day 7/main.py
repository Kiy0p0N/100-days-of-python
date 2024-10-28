import random
from hangman_words import word_list
from hangman_art import HANGMANPICS

print('WELCOME TO HANGMAN GAME!')

# Randomly selects a word from the word list
word = random.choice(word_list)
len_word = len(word)

# Sets up a placeholder to show the word length as underscores
placeholder = ['_' * len_word]
print(placeholder[0])

# Variables to hold guessed letters, display for the hidden word, and the player's lives
display = []
letter_list = []
lifes = 6

# Initializes the display with underscores for each letter in the chosen word
for i in range(0, len_word):
    display.append('_')

# Main game loop
while True:

    # If no lives are left, the player loses and the game ends
    if lifes == 0:
        print(f'The word was {word.upper()}')
        print('You lose!')
        break

    # If there are no underscores left, all letters have been guessed correctly
    if '_' not in display:
        print('Congratulations!')
        print('You win!')
        break

    guess = input('\nGuess a letter: ').lower()
    
    letter_list.append(guess)

    # Checks if the guessed letter is in the word
    if guess in word:
        # If so, it replaces the underscores in 'display' with the guessed letter in the correct positions
        for i in range(0, len_word):
            if word[i] == guess:
                display[i] = guess
    else:
        lifes -= 1

    # Prints the current state of the guessed word, remaining lives, and the list of guessed letters
    print(''.join(display))
    print(f'Lifes: {lifes}/6')
    print(letter_list)
    print(HANGMANPICS[lifes])  # Displays hangman art based on remaining lives