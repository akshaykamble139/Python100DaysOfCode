from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

stop_using_coffee_machine = False

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not stop_using_coffee_machine:
    user_choice = input(f" What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice == "off":
        stop_using_coffee_machine = True
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)






