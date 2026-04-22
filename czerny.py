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
        print(self.items)

    def buy(self):
        buying = input("Select")
        for x in self.items:
            if buying in self.items:
                Hero.inventory.append(x)
                Hero.balance - 5
                return x

James = Hero("James", [], 100, 1000)
Stock = Market(["Tape", "Chessboard", "Fig", "Shoes"])

while True:
    action = input("Do an action")
    if (action == "checkmarket") or (action == "check"):
        Stock.check()
    if (action == "buy") or (action == "purchase"):
        Stock.buy()