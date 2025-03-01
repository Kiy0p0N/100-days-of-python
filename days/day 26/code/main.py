import pandas as pd

nato_phonetic = pd.read_csv('nato_phonetic_alphabet.csv')  # Read csv file
nato_phonetic_dict = {letter:word for letter, word in nato_phonetic.values}  # Transform the file into a dictionary using Dictionary Comprehension

is_word = False
while not is_word:
    user_input = input("Enter a word: ").upper()  # Receives user input and returns the word in uppercase
    try:
        # Creates a list of words from the 'nato_phonetic_dict' dictionary using each letter of the user input as a key to find the word, which is the value
        converting_nato_phonetic = [nato_phonetic_dict[letter] for letter in user_input]

    except KeyError:  # If the user types something other than a letter of the alphabet
        print("Sorry, only letters in the alphabet.")

    else:
        print(converting_nato_phonetic)
        is_word = True  # If there are only letters of the alphabet the loop ends