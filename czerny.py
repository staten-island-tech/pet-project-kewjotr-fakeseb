import random
lottery = random.randint(0,5)
Tape = {
    "Name": "Tape",
    "Price": 2.00,
}




class Hero:
    def __init__(self, name, health, inventory, balance):
        self.name = name
        self.health = health
        self.inventory = inventory
        self.balance = balance

class Market:
    def marketitems(self):
        print("Tape", "Chess Board", "Heinz Ketchup", "Ice Cream", "Woodwork", "Sand", "Flag of Libya", "Plank", "Weedspray", "Turk", "Crusader Kings 3")

    def buy(self):


    def gamble(self, lottery):
        if lottery == 0:
            
    def choice(self, thetower):
        if thetower == "checkmarket" or thetower == "market":
            Market.marketitems()
        if thetower == "gamble":
            Market.gamble(lottery)

class payed_objected:
    def __init__(self,price):
        self.price = price


James = Hero("James", 100, "Silver Pot", 1000)
Tape = Market()

while True:
    thetower = input()
    Market.choice(thetower)