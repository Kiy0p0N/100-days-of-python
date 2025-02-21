import random

# Create lists with possible characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']


total_characters = [letters, numbers, symbols]  # Adding the lists to a new list

password = ''  # Create a variable to store the characters

number_of_characters = int(input('How many characters would you like in your password?\n'))

# The 'for' loop is repeated according to the number of times desired by the user
for i in range(1, number_of_characters + 1):
    
    # Randomly choose a list
    random_choice = random.randint(0, 2)  
    aleatory_list = total_characters[random_choice]

    aleatory_character_list = random.choice(aleatory_list)  # Randomly choose a character from the list

    password += aleatory_character_list  # Add the character to the password variable

print(password)