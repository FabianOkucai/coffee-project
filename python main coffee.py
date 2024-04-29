from menu import Menu, MenuItem
from coffee_making import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# coffee_maker.is_resource_sufficient()
coffee_machine = True
while coffee_machine == True:

    menu_item = Menu()
    coffee = menu_item.get_items()
    user_input = input(f"What would you like to have.{coffee} or report or off.\n")

    # coffee_maker.is_resource_sufficient(user_input)
    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        coffee_machine = False
        print("Come back later.")
    else:
        drink = menu_item.find_drink(user_input)
        coffee_maker.is_resource_sufficient(drink)
        cost = float()
        payment = money_machine.make_payment(cost)
        coffee_maker.make_coffee(drink)

        
        
        
    
        
        
        
        
        
        
        
    
    




    
    
    
    


