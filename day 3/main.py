# Welcome message
print('Welcome to the Treasure Hunt\n')

# First choice: right or left path
choose_1 = input('Choose a path: right or left\n')

# If the user chooses the right path
if choose_1 == 'right':
    print('Good choice, you walked a safe path until you arrived in front of the lake. \n')

    # Second choice: go around the lake or cross it in a boat
    choose_2 = input('Now choose: \n1- go around the lake. \n2- cross the lake in a small boat.\n')

    # If the user chooses to go around the lake, they encounter a dragon
    if choose_2 == '1':
        print('What bad luck... \nYou found a fire dragon waking up from its sleep while going around. \nGame over!')

    # If the user chooses to cross the lake safely, they reach a cave
    elif choose_2 == '2':
        print('Good choice, you crossed the lake safely and reached a cave.\n')

        # Third choice: pick a fork in the cave
        choose_3 = input("Inside the cave, you find 3 forks. \n1- You don't hear or feel anything. \n2- you feel a light breeze coming off of it. \n3- you hear some strange sounds \n")

        # If the user chooses the first fork, they encounter poisonous gas
        if choose_3 == '1':
            print('You feel your strength running out, the cave had poisonous gas. \nGame over!')

        # If the user chooses the second fork, they trigger a trap
        elif choose_3 == '2':
            print('In the first step you activate a trap. \nGame over!')

        # If the user chooses the third fork, they find the treasure
        elif choose_3 == '3':
            print('Congratulations!!!!!!!!!!!! \nYou arrive in a room full of gold, the noise you heard was just the sound of fairies playing.')

        # If the user enters any other option, they encounter monsters
        else:
            print('You decide to go back, but you come face to face with hungry monsters. \nGame over!')

    # If the user chooses to do something other than cross the lake, the game ends
    else:
        print('Oh noooo \nGame over!')

# If the user chooses the left path, they step on a snake
elif choose_1 == 'left':
    print('What bad luck... \nYou stepped on a poisonous snake.\nGame over!')

# If the user enters an invalid path, the game ends
else:
    print('This path does not exist. \nGame over!')
