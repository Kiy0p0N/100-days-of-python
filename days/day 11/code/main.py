import random
import art

def random_card():
    """Return a random number from the list of card values"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # List of possible card values
    return random.choice(cards)  # Randomly choose and return a card from the list

def calculate_score(cards):
    """Calculate and return the total score based on the cards"""
    if sum(cards) == 0 and len(cards) == 2:  # Check if the hand is a Blackjack (Ace + 10-value card)
        return 0  # Blackjack score (Ace as 11 and 10-value card)

    if 11 in cards and sum(cards) > 21:  # If there's an Ace (value 11) and the score exceeds 21
        cards.remove(11)  # Replace Ace with 1 to avoid going over 21
        cards.append(1)

    return sum(cards)  # Return the total score of the hand

def comparator(p_score, c_score):
    """Compare player's and computer's scores to determine the result"""
    if p_score == c_score:  # If both scores are equal, it's a draw
        return "Drawn"
    elif c_score == 0:  # If the computer has a Blackjack, the player loses
        return "You lose"
    elif p_score == 0:  # If the player has a Blackjack, the player wins
        return "You win"
    elif c_score > 21:  # If the computer exceeds 21, the player wins
        return "You win"
    elif p_score > 21:  # If the player exceeds 21, the player loses
        return "You lose"
    elif p_score > c_score:  # If the player's score is higher, the player wins
        return  "You win"
    else:  # Otherwise, the computer wins
        return "You lose"

def play_game():
    print(art.blackjack_art)  # Display the game's ASCII art (imported from the art module)

    player = []  # List to hold the player's cards
    computer = []  # List to hold the computer's cards

    player_score = -1  # Initial score of the player
    computer_score = -1  # Initial score of the computer

    game_over = False  # Flag to control when the game ends

    for _ in range(2):  # Deal 2 cards to both the player and the computer
        player.append(random_card())
        computer.append(random_card())

    while not game_over:  # Main game loop, continues until the game is over
        player_score = calculate_score(player)  # Update player's score
        computer_score = calculate_score(computer)  # Update computer's score

        print(f"    Your cards: {player}n current score: {player_score}")  # Display player's cards and score
        print(f"    Computer's first card: {computer[0]}")  # Display the computer's first card

        if player_score == 0 or computer_score == 0 or player_score > 21:  # Check for game-ending conditions
            game_over = True  # End the game if the player or computer has Blackjack or if the player busts
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")  # Ask player for input

            if another_card == "y":  # If player chooses to take another card
                player.append(random_card())  # Deal another card to the player
            else:
                game_over = True  # End the player's turn if they choose not to take another card

    while computer_score != 0 and computer_score < 17:  # Computer's turn (must draw if score is less than 17)
        computer.append(random_card())  # Deal another card to the computer
        computer_score = calculate_score(computer)  # Recalculate the computer's score

    print(f"    Your final hand: {player}, final score: {player_score}")  # Display final player's hand and score
    print(f"    Computer's final hand: {computer}, final score: {computer_score}")  # Display final computer's hand and score
    print(comparator(player_score, computer_score))  # Compare scores and print the result

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":  # Ask if the player wants to play again
    print("\n" * 20)  # Clear the screen for the new game
    play_game()  # Start a new game
