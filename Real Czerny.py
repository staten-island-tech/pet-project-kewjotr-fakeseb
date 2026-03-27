class Hero:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    
    def market(self, marketitems, balance):
        self.marketitems = marketitems()
        self.balance = balance
    
HA_Sosa = Hero("HA Sosa", 100, "Silver Pot")