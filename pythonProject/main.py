from sys import exit
import data
global money
money = 0


def report():
    print(f"Water: {data.resources['water']}\nMilk: {data.resources['milk']}\nCoffee: {data.resources['coffee']}\nMoney: ${money: .2f}")


def resources_suff(drink):
    if data.MENU[drink]['ingredients']['water'] <= data.resources['water']:
        if data.MENU[drink]['ingredients']['coffee'] <= data.resources['coffee']:
            if drink == "espresso":
                return True
            else:
                if data.MENU[drink]['ingredients']['milk'] <= data.resources['milk']:
                    return True
                else:
                    print("Sorry, there is not enough milk")
                    return False
        else:
            print("Sorry, there is not enough coffee")
            return False
    else:
        print("Sorry, there is not enough water")
        return False


def money_suff(tot_money, coffee):
    global money
    if tot_money >= data.MENU[coffee]["cost"]:
        change = round(tot_money - data.MENU[coffee]["cost"], 2)
        tot_money -= change
        money += tot_money
        print(f"Here is ${change} in change")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def deplete(drink):
    data.resources['water'] -= data.MENU[drink]['ingredients']['water']
    data.resources['coffee'] -= data.MENU[drink]['ingredients']['coffee']
    if drink != "espresso":
        data.resources['milk'] -= data.MENU[drink]['ingredients']['milk']


while True:
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    user_coffee = user_coffee.lower()

    if user_coffee == "off":
        exit()
    elif user_coffee == "report":
        report()
    else:
        is_resource_suff = resources_suff(user_coffee)
        if is_resource_suff:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            print(total)
            is_money_suff = money_suff(total, user_coffee)

            if is_money_suff:
                deplete(user_coffee)

# if user_coffee == "espresso":
