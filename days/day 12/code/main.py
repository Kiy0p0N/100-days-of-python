from random import randint
import art

def check_answer(user_guess, actual_answer):
    """Function to check the user's guess against the actual number"""
    if user_guess == actual_answer:
        print(f"You got it! The answer was {actual_answer}.")
        return 1  # Return 1 if the guess is correct
    elif user_guess > actual_answer:
        print("Too high.")
    else:
        print("Too low.")
    return 0  # Return 0 if the guess is incorrect

def choose_difficulty():
    """Function to set the difficulty level and return the number of attempts"""
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == "easy":
        return 10  # Easy gives 10 attempts
    return 5  # Hard gives 5 attempts

def game():
    """Main game function"""
    print(art.GUESS_NUMBER_LOGO)  # Display game logo
    print("Welcome to the Number Guessing Game!",
          "\nI'm thinking of a number between 1 and 100.")

    answer = randint(1, 100)  # Generate a random number between 1 and 100
    lives = choose_difficulty()  # Get the number of attempts based on difficulty

    game_over = False
    while not game_over:
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))  # Prompt user for a guess

        continue_game = check_answer(guess_number, answer)  # Check the user's guess

        if continue_game == 0:  # Incorrect guess
            lives -= 1  # Decrease the number of attempts
            if lives == 0:  # If no attempts are left
                print("You've run out of guesses. Refresh the page to run again.")
                game_over = True  # End game if the lives is equal 0
            else:
                print("Guess again.")  # Prompt to try again
        else:
            game_over = True  # End game if the guess is correct

# Entry point of the program
game()