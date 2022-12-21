MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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


def make_coffee(drink_type, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= MENU[drink_type]["ingredients"][item]
    return f"Here is your {drink_type}. Enjoy!"


make_coffee("espresso", MENU["espresso"]["ingredients"])

#print(MENU["espresso"]["ingredients"]["water"])