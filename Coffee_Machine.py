# coffee machine program
print("""   _____       __  __               __  __            _     _             
  / ____|     / _|/ _|             |  \/  |          | |   (_)            
 | |     ___ | |_| |_ ___  ___     | \  / | __ _  ___| |__  _ _ __   ___  
 | |    / _ \|  _|  _/ _ \/ _ \    | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \ 
 | |___| (_) | | | ||  __/  __/    | |  | | (_| | (__| | | | | | | |  __/ 
  \_____\___/|_| |_| \___|\___|    |_|  |_|\__,_|\___|_| |_|_|_| |_|\___| 
                                                                          
                                                                          """)

print('''                    (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \""--..__                              __..--""/
       '._     """----.....______.....----"""     _.'
          `""--..,,_____            _____,,..--""`
                        `"""----"""`
                        
                        ''')


print("for help write just 'help'")
coffee = 100
milk = 200
money = 0
water= 300

req_money = {"expresso": 1.50, "latte": 2.50, "cappuccino": 3.00}
req_water = {"expresso": 50, "latte": 200, "cappuccino": 250}
req_coffee = {"expresso": 18, "latte": 24, "cappuccino": 24}
req_milk = {"expresso": 0, "latte": 150, "cappuccino": 100}


def coffee_maker(coff_name, coffee, milk, water, money):
    milk -= req_milk[coff_name]
    water -= req_water[coff_name]
    coffee -= req_coffee[coff_name]
    money += req_money[coff_name]
    return  milk, water, coffee, money


def coins(coff_name):
    if water < req_water[coff_name]:
        print("Sorry there is not enough water.")
        return

    elif coffee < req_coffee[coff_name]:
        print("Sorry there is not enough coffee.")
        return

    elif milk < req_milk[coff_name]:
        print("Sorry there is not enough milk.")
        return

    print("Please insert coins!")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if total > req_money[coff_name]:
        change = total - req_money[coff_name]
        print(f"Here is ${change: .2f} in change")
        print(f"Here is your {coff_name}☕️. Enjoy!")
    elif total == req_money[coff_name]:
        print(f"Here is your {coff_name}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


while True:
    need = input("What would you like? (expresso/latte/cappuccino) ☕️: ").lower()
    if need == "off":
        break

    elif need == "report":
        print(f"""Water: {water}ml
Milk: {milk}ml
Coffee: {coffee}g
Money: $ {money}
""")

    elif need == "expresso":
        check = coins("expresso")
        if check != False:
            milk, water, coffee, money = coffee_maker("expresso", coffee, milk, water, money)

    elif need == "latte":
        check = coins("latte")
        if check != False:
            milk, water, coffee, money = coffee_maker("latte", coffee, milk, water, money)

    elif need == "cappuccino":
        check = coins("cappuccino")
        if check != False:
            milk, water, coffee, money = coffee_maker("cappuccino", coffee, milk, water, money)

    elif need == "help":
        print("""This is a Coffee Machine
There are 3 types of coffee
expresso = $ 1.50
latte = $ 2.50
cappuccino = $ 3.00
1 quarters = $0.25,
1 dimes = $0.10,
1 nickles = $0.05,
1 pennies = $0.01
report --> to check for resources
off --> to close the machine""")

    else:
        print("Invalid Input")
