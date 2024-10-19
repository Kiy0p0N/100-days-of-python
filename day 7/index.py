import random
from hangman_words import word_list
from hangman_art import HANGMANPICS

print('WELCOME TO HANGMAN GAME!')

word = random.choice(word_list)
len_word = len(word)

placeholder = ['_'* len_word]
print(placeholder[0])


display = []
letter_list = []
lifes = 6

for i in range(0, len_word):
    display.append('_')


while True:

    if lifes == 0:
        print(f'The word was {word.upper()}')
        print('You lose!')
        break

    if '_' not in display:
        print('Congratulations!')
        print('You win!')
        break


    guess = input('\nGuess a letter: ').lower()

    letter_list.append(guess)
    
    if guess in word:     
        for i in range(0, len_word):
            if word[i] == guess:
                display[i] = guess
            else:
                continue

        

    elif guess not in word:
        lifes -= 1

    print(''.join(display))
    print(f'Lifes: {lifes}/6')
    print(letter_list)    
    print(HANGMANPICS[lifes])