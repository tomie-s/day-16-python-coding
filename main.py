from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
machine = CoffeeMaker()
bank = MoneyMachine()


machine_on = True

while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")

    if choice == "off":
        machine_on = False
    elif choice == "report":
        machine.report()
        bank.report()
    else:
        drink = menu.find_drink(choice)
        if machine.is_resource_sufficient(drink) and bank.make_payment(drink.cost):
            machine.make_coffee(drink)
