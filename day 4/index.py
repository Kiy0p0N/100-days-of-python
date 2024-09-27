import random

print('Welcome to game!')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''

paper ='''
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

choices = [rock, paper, scissors]

your_choice = int(input('Enter 0 for Rock, 1 for Paper or 2 for Scissors: '))

if 0 <= your_choice < 3:
    print('\nYour choice: \n')
    print(choices[your_choice])

    print('\nComputer choice: \n')
    random_choice = random.randint(0, 2)
    print(choices[random_choice])

    if your_choice == random_choice:
        print('DRAWN!')
    elif (your_choice == 0 and random_choice == 2) or (your_choice == 1 and random_choice == 0) or (your_choice == 2 and random_choice == 1):
        print('You WIN!')
    else:
        print('You LOSE!')

else:
    print('You typed a invalid number. You LOSE!')