import random
lottery = random.randint(0,5)

class Hero:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory

class shopping:    
    def market(self, marketitems, balance):
        self.marketitems = marketitems()
        self.balance = balance

    def gamble(self, lottery):
        if lottery == 0:
    
James = Hero("James", 100, "Silver Pot")