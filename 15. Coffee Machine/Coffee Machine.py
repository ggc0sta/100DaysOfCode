    # Goal: https://replit.com/@appbrewery/coffee-machine-final?embed=1&output=1#main.py

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


profit = 0


def enough_resources(order_ingredients):
    """Returns True or False if resources are sufficient to make drink"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_enough = False
    return is_enough


def process_coins(total_cost):
    """Returns the total calculated from coins inserted"""
    print(f"Your total is ${total_cost}. Please insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Returns True when the payment is accepted, and false when not"""
    if money_received >= drink_cost:
        global profit  # using global variable profit"
        profit += drink_cost

        if money_received > drink_cost:
            change = round(money_received - drink_cost, 2)
            print(f"Here is ${change} dollars in change.")

        return True
    else:
        print("Sorry, you didn't insert enough coins. Here is your money back.")
        return False


def make_coffee(drink_type, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in drink_ingredients:
        resources[item] -= MENU[drink_type]["ingredients"][item]
    return f"Here is your ☕️ {drink_type}. Enjoy!"


is_on = True

while is_on:

    # TODO: [OK] 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: [OK] 2. Turn off machine
    if choice == "off":
        print("off")
        is_on = False

    # TODO: [OK] 3. print a report of all coffee machine resources
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        # TODO: 4. Check resources sufficient to make drink order
        if enough_resources(drink["ingredients"]):
            cash_received = process_coins(drink['cost'])
            if is_transaction_successful(cash_received, drink["cost"]):
                print(make_coffee(choice, drink["ingredients"]))

    else:
        print("invalid order")

