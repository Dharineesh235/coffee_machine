from menu import MENU, resources
import os


def func():
    # os.system('clear')
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    user_choice_details = {}
    resource_report = resources
    if user_choice == 'espresso' or user_choice == 'latte' or user_choice == 'cappuccino':
        if user_choice == 'espresso':
            user_choice_details = MENU["espresso"]
        if user_choice == 'latte':
            user_choice_details = MENU["latte"]
        if user_choice == 'cappuccino':
            user_choice_details = MENU['cappuccino']
    elif user_choice == 'report':
        print(f'''
            water:{resources["water"]},
            "milk": {resources["milk"]},
            "coffee": {resources["coffee"]},
        ''')
    else:
        print('Invalid Input')

    if resources['water'] < user_choice_details['ingredients']['water'] and resources['coffee'] < \
            user_choice_details['ingredients']['coffee']:
        for key in resources:
            print(f'{key}:{resources[key]}')
    else:
        quarters = int(input("quarters : "))
        dimes = int(input("dimes : "))
        nickles = int(input("nickles : "))
        pennies = int(input("pennies : "))
        dollar = round((quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01), 1)
        print(dollar)
        if dollar > user_choice_details['cost']:
            resource_report['water'] = resources['water'] - user_choice_details['ingredients']['water']
            resource_report['milk'] = resources['milk'] - user_choice_details['ingredients']['milk']
            resource_report['coffee'] = resources['coffee'] - user_choice_details['ingredients']['coffee']
            print(f"your {user_choice} is ready")

    print(resource_report)
    func()


func()
