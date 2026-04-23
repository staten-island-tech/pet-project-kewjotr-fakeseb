import random

class Hero:
    def __init__(self, name, inventory, health, balance):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.balance = balance

class Fighting:
    def __init__(self):
        pass
    def gilbert(self, monster):
        pass

class Event:
    def __init__(self):
        pass
    def maximum(self, number):
        pass

class Market:
    def __init__(self,items):
        self.items = items
    
    def check(self):
        print(self.items)

    def buy(self,hero_obj):
        buying = input("Select")
        for x in self.items:
            if buying in self.items:
                hero_obj.inventory.append(x)
                hero_obj.balance - 5
                return x

James = Hero("James", [], 100, 1000)
Stock = Market(["Tape", "Chessboard", "Fig", "Shoes"])

print(James)

while True:
    action = input("Do an action")
    spawn = random.randint(0, 10)
    if spawn < 8:
        if (action == "checkmarket") or (action == "check"):
            Stock.check()
        elif (action == "buy") or (action == "purchase"):
            Stock.buy(James)
        elif (action == "checkinventory") or (action == "inventory"):
            print(James.inventory)