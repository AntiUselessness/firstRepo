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
    "money": 0
}

user_coins = 0


def coins():
    global user_coins
    user_q = int(input("How many quarters: "))
    user_d = int(input("How many dimes: "))
    user_n = int(input("How many nickles: "))
    user_p = int(input("How many pennies: "))
    q = int(user_q) * 0.25
    d = int(user_d) * 0.10
    n = int(user_n) * 0.05
    p = int(user_p) * 0.01
    user_coins = float(round(q + d + n + p, 2))
    return f"Your total coins: ${user_coins}"


espresso_water = MENU['espresso']['ingredients']['water']
espresso_coffee = MENU['espresso']['ingredients']['coffee']
espresso_cost = float(MENU['espresso']['cost'])
latte_water = MENU['latte']['ingredients']['water']
latte_coffee = MENU['latte']['ingredients']['coffee']
latte_milk = MENU['latte']['ingredients']['milk']
latte_cost = float(MENU['latte']['cost'])
cap_water = MENU['cappuccino']['ingredients']['water']
cap_milk = MENU['cappuccino']['ingredients']['milk']
cap_coffee = MENU['cappuccino']['ingredients']['coffee']
cap_cost = float(MENU['cappuccino']['cost'])

print("** WELCOME TO THE ZEZO COFFEE MACHINE **\n")

still_order = True
while still_order:
    user_order = input(
        """What would you like to order?
1. Espresso ($1.5)
2. Latte ($2.5)
3. Cappuccino ($3)\n
=> Type 'report' to see the coffee machine's current resource values.\n
Insert here: """).casefold()

    if user_order == "off":
        print("You turned off the coffee machine....")
        still_order = False
    elif user_order == "report":
        for i in resources:
            print(f"{i}: {resources[i]}")
    elif user_order == "1":
        if resources['water'] >= espresso_water and resources['coffee'] >= espresso_coffee:
            print("** INSERT COINS **\n")
            x = coins()
            print(x)
            if user_coins == espresso_cost:
                change = 0
                print("Your money is enough. Here is your espresso. Enjoy!\n")
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins > espresso_cost:
                change = user_coins - espresso_cost
                print(f"Here is your change: ${change}\n")
                print("And here is your espresso. Enjoy!\n")
                resources['water'] = resources['water'] - espresso_water
                resources['coffee'] = resources['coffee'] - espresso_coffee
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins < espresso_cost:
                print("Sorry. That's not enough money. Money refunded....")
        else:
            print("Sorry, there is not enough ingredients to make espresso....\n")
    elif user_order == "2":
        if resources['water'] >= latte_water and resources['coffee'] >= latte_coffee and resources[
                'milk'] >= latte_milk:
            print("** INSERT COINS **\n")
            x = coins()
            print(x)
            if user_coins == latte_cost:
                change = 0
                print("Your money is enough. Here is your latte. Enjoy!\n")
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins > latte_cost:
                change = user_coins - latte_cost
                print(f"Here is your change: ${change}\n")
                print("And here is your latte. Enjoy!\n")
                resources['water'] = resources['water'] - latte_water
                resources['coffee'] = resources['coffee'] - latte_coffee
                resources['milk'] = resources['milk'] - latte_milk
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins < latte_cost:
                print("Sorry. That's not enough money. Money refunded....")
        else:
            print("Sorry, there is not enough ingredients to make latte....\n")
    elif user_order == "3":
        if resources['water'] >= cap_water and resources['milk'] >= cap_milk and resources['coffee'] >= cap_coffee:
            print("** INSERT COINS **\n")
            x = coins()
            print(x)
            if user_coins == cap_cost:
                change = 0
                print("Your money is enough. Here is your cappuccino. Enjoy!\n")
                resources['water'] = resources['water'] - cap_water
                resources['coffee'] = resources['coffee'] - cap_coffee
                resources['milk'] = resources['milk'] - cap_milk
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins > cap_cost:
                change = user_coins - cap_cost
                print(f"Here is your change: ${change}\n")
                print("And here is your cappuccino. Enjoy!\n")
                resources['water'] = resources['water'] - cap_water
                resources['coffee'] = resources['coffee'] - cap_coffee
                resources['milk'] = resources['milk'] - cap_milk
                resources['money'] = resources['money'] + (user_coins - change)
            elif user_coins < latte_cost:
                print("Sorry. That's not enough money. Money refunded....")
        else:
            print("Sorry, there is not enough ingredients to make cappuccino....\n")
    else:
        print("You did not type the right number! Try again....\n")
