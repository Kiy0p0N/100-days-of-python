# higher vs lower game
# choose two people from the list of instagram accounts and compare to see who has the most followers

from random import randint

import art
import instagram
instagram_accounts = instagram.instagram_list

# 1 - choose two random numbers
def random_number():
    len_instagram_list = len(instagram.instagram_list)
    number = randint(1, len_instagram_list)

    return number

# 2 - Compare the number of followers and return the highest
def compare_follower(acc_a, acc_b):
    if acc_a["followers"] > acc_b["followers"]:
        return acc_a
    return acc_b

# main function
def game():

    score = 0

    number_a = random_number()
    account_a = instagram_accounts[number_a]

    # 3 - create a loop that continues until the user makes a mistake
    game_over = False
    while not game_over:

        # selects a new account, different from 'account_a' on each new round
        number_b = random_number()
        while number_a == number_b:
            number_b = random_number()
        account_b = instagram_accounts[number_b]

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
                number_a = number_b
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