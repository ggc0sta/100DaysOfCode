from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

mastrena = CoffeeMaker()
cash_register = MoneyMachine()
MENU = Menu()

is_on = True

while is_on:
    choice = input(f"What would you like? {MENU.get_items()}: ").lower()

    if choice == "off":
        print("off")
        is_on = False
    elif choice == "report":
        mastrena.report()
        cash_register.report()
    else:
        # Choice is a drink
        drink = MENU.find_drink(choice)

        if mastrena.is_resource_sufficient(drink):
            if cash_register.make_payment(drink.cost):
                mastrena.make_coffee(drink)


