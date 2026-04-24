import random

events = ["None", "None", "None", "None","None", "None", "None", "None", "Hound", "Gargoyle", "Sauron", "Nezhmetdinov"]

class Hero:
    def __init__(self, name, inventory, health, balance):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.balance = balance
    
    def regeneration(self):
        if Hero.health < 100:
            Hero.health + 5
        else:
            Hero.health == 100
class Fighting:
    def __init__(self):
        pass
    def gilbert(self, number):
        monster = events[number]

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
Battle = Fighting()

while James.health != 0:
    spawn = random.randint(0, 11)
    James.regeneration()
    if spawn < 8:
        action = input("Do an action")
        if (action == "checkmarket") or (action == "check"):
            Stock.check()
        elif (action == "buy") or (action == "purchase"):
            Stock.buy(James)
        elif (action == "checkinventory") or (action == "inventory"):
            print(James.inventory)
    else:
        Battle.gilbert(spawn)