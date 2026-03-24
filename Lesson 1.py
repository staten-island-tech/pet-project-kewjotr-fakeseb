
# Activity 1

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Ernst = Hero("Ernst", 1000000, ["Flag of Libya"])

Ernst.buy({"title": "Toyota", "speed": 90, "atk": 380})
print(Ernst.__dict__)