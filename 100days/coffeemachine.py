
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
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappucino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

def print_report():
    """Print report of resources and money"""
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:   {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money:  ${money:.2f}")

def turn_off():
    """Powers off Coffee Machine (exits program)"""
    global power
    power = "off"
    print("Powering off...")

def check_resources(drink):
    """Checks that there is enough ingredients to make the drink.
       Returns 'sufficient' or resource name that is lacking"""
    for key, value in MENU[drink]['ingredients'].items():
        if value > resources[key]:
            return key
    return "sufficient"

def make_coffee(drink):
    """Deducts system resources used to make the coffee drink"""
    for key, value in MENU[drink]['ingredients'].items():
        resources[key] -= value

def brew_beverage(drink):
    """Makes coffee when there are sufficient resources and the customer has paid"""
    status = check_resources(drink)
    if status == "sufficient":
        amount_paid = process_coins()
        paid = check_transaction(amount_paid, drink)
        if paid:
            make_coffee(drink)
            print(f"Here is your {drink}. Enjoy!")
    else:
        print(f"Sorry there is not enough {status}")

def process_coins():
    """Gets coins from customer and returns total amount paid"""
    paid_coins = {
            "quarters": 0,
            "dimes": 0,
            "nickels": 0,
            "pennies": 0
        }
    print("Please insert coins.")
    for key in paid_coins.keys():
        paid_coins[key] = get_coins(key)
    return count_coins(paid_coins)

def get_coins(coin):
    """Returns a valid integer input"""
    while True:
        count = input(f"How many {coin}?: ")
        try:
            count = int(count)
            return count
        except ValueError:
            print("Invalid Entry")

def check_transaction(amount_paid, drink):
    """Checks to see if the customer paid for the drink and gives change"""
    if amount_paid < MENU[drink]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global money
        money += MENU[drink]["cost"]
        if amount_paid > MENU[drink]["cost"]:
            change = amount_paid - MENU[drink]["cost"]
            print(f"Here is ${change} dollars in change")
        return True

def count_coins(coins):
    """Returns the sum of all coins"""
    values = [0.25, 0.1, 0.05, 0.01]
    total = [a * b for a, b in zip(coins.values(), values)]
    # total = coins['quarters'] * 0.25 + coins['dimes'] * 0.10 + coins['nickels'] * 0.05 + coins['pennies'] * 0.01
    return round(sum(total),2)

if __name__ == "__main__":

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }
    money = 0
    choice_map = {
        "report": print_report,
        "off": turn_off,
        "espresso": lambda: brew_beverage("espresso"),
        "latte": lambda: brew_beverage("latte"),
        "cappucino": lambda: brew_beverage("cappucino")
    }

    power = "on"
    while power == "on":
        valid_choice = False
        while not valid_choice:
            choice = input("What would you like?(espresso/latte/cappucino): ")
            if choice in choice_map:
                valid_choice = True
        choice_map[choice]()

