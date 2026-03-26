# Activity 1

class pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

    def play(self, moraleincreasement):
        self.__happiness += moraleincreasement

    def show_status(self):
        print("Sipke happiness value is now",self.__happiness)

    def tick(self, Action):
        if Action == "play":
            Sipke.play(2)
        if Action == "status":
            Sipke.show_status()
        if Action == "wash":
            Sipke.play(-3)

Sipke = pet("Sipke", 5)

while True:
    Action = input("Do an action\n")
    Sipke.tick(Action)