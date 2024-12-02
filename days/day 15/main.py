MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100
        },
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "coffee": 100,
    "milk": 200
}

# TODO: 4. Check resources sufficient?
def enough_resources (coffee):
    """Returns false if there are not enough ingredients to make the drink or true if there are"""
    for item in coffee:
        if resources[item] < coffee[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# TODO: 5. Process coins.
def process_coins ():
    """Returns the calculated total of the coins entered"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickels? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01

    return total

# TODO: 6. Check transaction successful?
def check_transaction (money_received, coffee_cost):
    """Returns the change and true if there is enough money or returns false if there is not enough money"""
    if money_received >= coffee_cost:
        if money_received > coffee_cost:
            change = money_received - coffee_cost
            print(f"Here is {round(change, 2)} dollars in change.")

        global money
        money += coffee_cost
        return True

    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# TODO: 7. Make Coffee.
def make_coffee (ingredients):
    """Uses the resources to make a drink"""
    for item in ingredients:
        resources[item] -= ingredients[item]


# main
money = 0

is_on = True

while is_on:
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice in MENU:
        if enough_resources(MENU[choice]["ingredients"]):
            payment = process_coins()
            if check_transaction(payment, MENU[choice]["cost"]):
                make_coffee(MENU[choice]["ingredients"])
                print(f"Here is your {choice}. Enjoy")

            else:
                print("Sorry that's not enough money. Money refunded.")
                is_on = False

        else:
            is_on = False


    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif choice == "off":
            is_on = False

    # TODO: 3. Print report.
    elif choice == "report":
        print(f"Water: {resources["water"]}ml \nMilk: {resources["milk"]}ml \nCoffee: {resources["coffee"]}g \nMoney: ${money}")

    else:
            print("Sir, we don't have that on our menu.")