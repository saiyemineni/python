from flavours import MENU, resources


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry! there is not enough {item}")
            return False
    return True


def process_coin():
    """return total calculated from coins inserted"""
    print("Please insert coin.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dims?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_sucessful(money_received, drink_cost):
    """Return tru if transaction is sucessful, False if money is insufficient"""
    if money_received >= drink_cost:
        change_money = round(money_received - drink_cost, 2)
        print(f"Here is ${change_money} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


profit = 0
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"profit: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_sucessful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
