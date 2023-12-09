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


def has_enough_resources(coffee_type, resources):
    """Checks if the coffee machine has enough resources to make the coffee"""
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        required_water = MENU[coffee_type]["ingredients"]["water"] if "water" in MENU[coffee_type]["ingredients"] else 0
        required_milk = MENU[coffee_type]["ingredients"]["milk"] if "milk" in MENU[coffee_type]["ingredients"] else 0
        required_coffee = MENU[coffee_type]["ingredients"]["coffee"] if "coffee" in MENU[coffee_type][
            "ingredients"] else 0

        return current_water >= required_water and current_milk >= required_milk and current_coffee >= required_coffee
    else:
        return False


def use_resources(coffee_type, resources):
    """Consumes the resources in coffee machine to make the drink"""
    current_water = resources["water"]
    current_milk = resources["milk"]
    current_coffee = resources["coffee"]

    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        required_water = MENU[coffee_type]["ingredients"]["water"] if "water" in MENU[coffee_type]["ingredients"] else 0
        required_milk = MENU[coffee_type]["ingredients"]["milk"] if "milk" in MENU[coffee_type]["ingredients"] else 0
        required_coffee = MENU[coffee_type]["ingredients"]["coffee"] if "coffee" in MENU[coffee_type][
            "ingredients"] else 0

        resources["water"] = current_water - required_water
        resources["milk"] = current_milk - required_milk
        resources["coffee"] = current_coffee - required_coffee

    return resources


def print_resources(machine_resources):
    """Prints current resources in the coffee machine"""
    current_water = machine_resources["water"]
    current_milk = machine_resources["milk"]
    current_coffee = machine_resources["coffee"]
    current_money = machine_resources["money"] if "money" in machine_resources else 0

    print(f"Water: {current_water}ml")
    print(f"Milk: {current_milk}ml")
    print(f"Coffee: {current_coffee}g")
    print(f"Money: ${current_money}")


stop_using_coffee_machine = False


def process_money():
    """Processes the amount received from the coins inserted in the coffee machine"""
    print("Please insert coins.")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.10
    return quarters + dimes + nickles + pennies


while not stop_using_coffee_machine:
    user_choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        print_resources(resources)
    elif (user_choice == "espresso" or user_choice == "latte" or
          user_choice == "cappuccino") and has_enough_resources(user_choice, resources):
        total_money_paid = process_money()

        if total_money_paid >= MENU[user_choice]["cost"]:
            change_to_return = total_money_paid - MENU[user_choice]["cost"]
            print(f"Here is ${change_to_return} in change.")
            print(f"Here is your {user_choice} ☕. Enjoy!")
            resources = use_resources(user_choice, resources)
            resources["money"] = resources["money"] + MENU[user_choice]["cost"] if "money" in resources else \
            MENU[user_choice]["cost"]
        else:
            print("Sorry that's not enough money. Money refunded")

    elif user_choice == "off":
        stop_using_coffee_machine = True
