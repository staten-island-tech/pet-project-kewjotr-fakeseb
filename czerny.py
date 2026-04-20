class Objects:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Hero:
    def __init__(self, name, health, balance):
        self.name = name
        self.health = health
        self.inventory = []
        self.balance = balance

class Market:
    def __init__(self,items):
        self.items = items
    def marketitems(self):
        print(Market.items)
    def buy(self):
        purchase = input()
        Hero.balance - Objects.price
    def choice(self, thetower):
        if thetower == "checkmarket" or thetower == "market":
            Market.marketitems()
        if thetower == "buy" or thetower == "purchase":
            Market.buy()

class payed_objected:
    def __init__(self,price):
        self.price = price


James = Hero("James", 100, 1000)

while True:
    thetower = input()
    Market.choice(thetower)