from variables import MENU
from variables import resources

class coffee_machine:
    profit = 0.0

    def __init__(self):
        self.start_coffee_machine()

    def start_coffee_machine(self):
        is_machine_on = True

        while is_machine_on:
            user_input = input("What would you like? (espresso/latte/cappuccino): ")

            if user_input == "off":
                is_machine_on = False
                return exit("Machine is shutting down... off.")
            elif user_input == "report":
                self.report_machine_status()
            else:
                self.make_hot_beverage(user_input)

    def process_payment(self, beverage_cost) -> bool:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01

        total_money = quarters + dimes + nickles + pennies

        if total_money >= beverage_cost:
            self.profit += beverage_cost
            change = total_money - beverage_cost
            if change > 0:
                print(f"Here is ${round(change, 2)} in change")
            return True
        else:
            print("Sorry that's not enough money. Money refunded")
            return False

    def make_hot_beverage(self, beverage_name):
        try:
            beverage = MENU[beverage_name]
            beverage_ingredients = beverage['ingredients']
            if self.resources_are_available(beverage_ingredients):
                if self.process_payment(beverage['cost']):
                    self.prepare_beverage(beverage_ingredients)
                    print(f"Here is your {beverage_name}, Enjoy it!")
        except Exception as error:
            print(f"Beverage not found {error}")

    def resources_are_available(self, beverage_ingredients) -> bool:
        can_make_beverage = True
       
        for ingredient in beverage_ingredients:
            if resources[ingredient] < beverage_ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                can_make_beverage = False
        
        return can_make_beverage

    def prepare_beverage(self, beverage_ingredients):
        for ingredient in beverage_ingredients:
            resources[ingredient] -= beverage_ingredients[ingredient]
        

    def report_machine_status(self):
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${self.profit}")

coffee_machine()