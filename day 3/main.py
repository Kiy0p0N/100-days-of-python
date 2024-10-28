print('Welcome to the Treasure Hunt\n')

choose_1 = input('Choose a path: right or left\n')

if choose_1 == 'right':
    print('Good choice, you walked a safe path until you arrived in front of the lake. \n')

    choose_2 = input('Now choose: \n1- go around the lake. \n2- cross the lake in a small boat.\n')

    if choose_2 == '1':
        print('What bad luck... \nYou found a fire dragon waking up from its sleep while going around. \nGame over!')

    elif choose_2 == '2':
        print('Good choice, you crossed the lake safely and reached a cave.\n')

        choose_3 = input("Inside the cave, you find 3 forks. \n1- You don't hear or feel anything. \n2- you feel a light breeze coming off of it. \n3- you hear some strange sounds \n")

        if choose_3 == '1':
            print('You feel your strength running out, the cave had poisonous gas. \nGame over!')
        elif choose_3 == '2':
            print('In the first step you activate a trap. \nGame over!')
        elif choose_3 == '3':
            print('Congratulations!!!!!!!!!!!! \nYou arrive in a room full of gold, the noise you heard was just the sound of fairies playing.')
        else:
            print('You decide to go back, but you come face to face with hungry monsters. \nGame over!')
        

    else:
        print('Oh noooo \nGame over!')

elif choose_1 == 'left':
    print('What bad luck... \nYou stepped on a poisonous snake.\nGame over!')

else:
    print('This path does not exist. \nGame over!')