class Hero:
    def __init__(self, name, health, balance):
        self.name = name
        self.health = health
        self.inventory = []
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
                Hero.inventory.append(Market.items(x))

James = Hero("James", 100, 1000)
Stock = Market("")

while True:
    action = input("Do an action")
    if (action == "checkmarket") or (action == "check"):
        Stock.check()
    if (action == "buy") or (action == "purchase"):
        Stock.buy()