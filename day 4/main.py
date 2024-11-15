import random

print('Welcome to game!')  # Welcome message for the game

# ASCII art for rock, paper, and scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]  # List of the choices (rock, paper, scissors)

# Get player's choice
your_choice = int(input('Enter 0 for Rock, 1 for Paper or 2 for Scissors: '))

if 0 <= your_choice < 3:  # Check if the input is valid (0, 1, or 2)
    print('\nYour choice: \n')
    print(choices[your_choice])  # Print the player's choice

    print('\nComputer choice: \n')
    random_choice = random.randint(0, 2)  # Randomly select the computer's choice
    print(choices[random_choice])  # Print the computer's choice

    # Determine the result of the game
    if your_choice == random_choice:
        print('DRAWN!')  # If both choices are the same, it's a draw
    elif (your_choice == 0 and random_choice == 2) or (your_choice == 1 and random_choice == 0) or (your_choice == 2 and random_choice == 1):
        print('You WIN!')  # Winning conditions
    else:
        print('You LOSE!')  # Losing conditions

else:
    print('You typed an invalid number. You LOSE!')  # Invalid input handling
