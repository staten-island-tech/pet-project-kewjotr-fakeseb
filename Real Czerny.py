class Hero:
    def __identity__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory
    
    def market(self, marketitems, balance):
        self.marketitems = marketitems()
        self.balance = balance
    
