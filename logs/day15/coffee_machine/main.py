
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


money_earned = 0.0


def check_resources(drink_ingredients):
    '''Will take the dictionary input and loop for each ingredient to check if there is enough of said ingredient. 
    If there are enough resources, it will return True, if there are not, it will return Fals'''
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True
        
    
def check_coins():
    '''Returns total value of coins that have been inserted'''
    print("\nPlease insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def process_transaction(money_payed, drink_price):
    '''Return True when payment is complete or False when funds are insuficient to complete transaction.'''
    if money_payed >= drink_price:
        change = round(money_payed - drink_price, 2)
        print(f"Here is ${change} in change.")
        global money_earned
        money_earned += drink_price
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_drink(drink_name, drink_ingredients):
    '''Deduct the required ingredients from the resources list.'''
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"\nHere is your {drink_name} ☕. Enjoy!\n")

print("\nMENU")
print("Espresso - $1.50\nLatte - $2.50\nCapuccino - $3.00\n")

def machine_func():
    machine_off = False
    while not machine_off:
        choice = input("What yould you like? (Espresso/Latte/Cappuccino): ").lower()
        if choice == "off":
            machine_off = True
        elif choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money_earned}")
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            drink = MENU[choice]
            if check_resources(drink['ingredients']):
                payment = check_coins()
                if process_transaction(payment, drink['cost']):
                    make_drink(choice, drink['ingredients'])
        else:
            print("I am sorry. That item is not available.")


machine_func()
