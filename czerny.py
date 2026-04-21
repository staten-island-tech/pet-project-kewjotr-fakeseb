class Hero:
    def __init__(self, name, inventory, health, balance):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.balance = balance

class Market:
    def __init__(self,items):
        self.items = items
    
    def check(self):
        print(Market.items)

    def buy(self):
        buying = input("Select")
        for x in Market.items:
            if buying in Market.items:
                signal = True
                return x

James = Hero("James", [], 100, 1000)
Stock = Market("")

while True:
    signal = False
    action = input("Do an action")
    if (action == "checkmarket") or (action == "check"):
        Stock.check()
    if (action == "buy") or (action == "purchase"):
        Stock.buy()
        if signal == True:
            James.inventory.append(x)
