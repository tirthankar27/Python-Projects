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
    "money": 0
}

def is_sufficient(r,m):
    if m == MENU['espresso']['ingredients']:
        if r['water'] < m['water'] or resources['coffee'] < m['coffee']:
            return False
    elif r['water'] < m['water'] or resources['milk'] < m['milk'] or resources['coffee'] < m['coffee']:
        return False
    return True

def sufficient_coins(x,y):
    return x-y

def resource_calculation(r,m):
    r['water'] = r['water'] - m['water']
    r['milk'] = r['milk'] - m['milk']
    r['coffee'] = r['coffee'] - m['coffee']
    r['money'] += m["cost"]

while True:
    choice = input("What would you like? (espresso / latte / cappuccino): ")
    if choice == 'off':
        break
    elif choice == "report":
        for key,value in resources.items():
            if key == "money":
                print(f"{key}: ${value}")
                continue
            if key == "coffee":
                print(f"{key}: {value}g")
                continue
            print(f"{key}: {value}ml")
    elif choice == "espresso":
        if not is_sufficient(resources,MENU['espresso']['ingredients']):
            print("Sorry insufficient resources")
        else:
            coin=float(input("Please insert coin: "))
            change=sufficient_coins(coin,MENU["espresso"]["cost"])
            if change>0:
                print(f"Please collect the change ${change}")
            elif change<0:
                print(f"Not enough money. Please collect the refund")
                continue
            resources['water'] = resources['water'] - MENU["espresso"]['ingredients']['water']
            resources['coffee'] = resources['coffee'] - MENU["espresso"]['ingredients']['coffee']
            resources['money']+=MENU["espresso"]["cost"]
            print("Enjoy your espresso")
    elif choice == "latte":
        if not is_sufficient(resources,MENU['latte']['ingredients']):
            print("Sorry insufficient resources")
        else:
            coin=float(input("Please insert coin: "))
            change=sufficient_coins(coin,MENU["latte"]["cost"])
            if change>0:
                print(f"Please collect the change ${change}")
            elif change<0:
                print(f"Not enough money. Please collect the refund")
                continue
            resource_calculation(resources,MENU['latte']['ingredients'])
            print("Enjoy your latte")
    elif choice == "cappuccino":
        if not is_sufficient(resources, MENU['cappuccino']['ingredients']):
            print("Sorry insufficient resources")
        else:
            coin=float(input("Please insert coin: "))
            change=sufficient_coins(coin,MENU["cappuccino"]["cost"])
            if change>0:
                print(f"Please collect the change ${change}")
            elif change<0:
                print(f"Not enough money. Please collect the refund")
                continue
            resource_calculation(resources,MENU['cappuccino']['ingredients'])
            print("Enjoy your cappuccino")
