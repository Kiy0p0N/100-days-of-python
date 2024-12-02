from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    # TODO: 1. Print report
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        coffee = menu.find_drink(choice)

        if coffee:
            # TODO: 2. Check resources
            is_sufficient = coffee_maker.is_resource_sufficient(coffee)
            if is_sufficient:
                # TODO: 3. Process coins
                payment_sufficient = money_machine.make_payment(coffee.cost)

                # TODO: 4. Check transition successful
                if payment_sufficient:
                    # TODO: 5. Make coffee
                    coffee_maker.make_coffee(coffee)

                else:
                    payment_sufficient
            else:
                is_sufficient
        else:
            coffee




# TODO: 5. Make coffee

