# higher vs lower game
# choose two people from the list of instagram accounts and compare to see who has the most followers

from random import choice

import art
from instagram import instagram_list

# Compare the number of followers and return the highest
def compare_follower(acc_a, acc_b):
    if acc_a["followers"] > acc_b["followers"]:
        return acc_a
    return acc_b

# main function
def game():

    score = 0

    account_a = choice(instagram_list)

    # create a loop that continues until the user makes a mistake
    game_over = False
    while not game_over:

        # selects a new account, different from 'account_a' on each new round
        account_b = choice(instagram_list)
        while account_a == account_b:
            account_b = choice(instagram_list)

        if score != 0:
            print(f"\nYou're right! Current score: {score}.")

        print(f"Compare A: {account_a["name"]}, a {account_a["profession"]}, from {account_a["country"]}.")
        print(art.vs)
        print(f"Compare B: {account_b["name"]}, a {account_b["profession"]}, from {account_b["country"]}.")

        user_choose = input("Who has more followers? Type 'A' or 'B': ").lower()

        more_followers = compare_follower(account_a, account_b)  # receive the account that has the most followers

        if user_choose == "a":
            if account_a == more_followers:
                score += 1
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_over = True

        elif user_choose == "b":
            if account_b == more_followers:
                score += 1

                # updates variables 'A' to variables 'B' so that it is the first option to be displayed in the next iteration of the loop
                account_a = account_b
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                game_over = True

        else:
            print("There is no such option. Game over for you!")
            game_over = True

# main code
print(art.logo)

game()