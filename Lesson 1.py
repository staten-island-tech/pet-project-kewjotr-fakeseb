# Activity 1

class pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

    def play(self, moraleincreasement):
        self.__happiness += moraleincreasement

    def show_status(self):
        print("Sipke happiness value is now",self.__happiness)

Sipke = pet("Sipke", 5)

Action = input("Select action\n")
if Action == "play":
    Sipke.play(2)
if Action == "status":
    Sipke.show_status()
if Action == "wash":
    Sipke.play(-3)
while Action != "end":
    Action = input("Select action\n")
    if Action == "play":
        Sipke.play(2)
    if Action == "status":
        Sipke.show_status()
    if Action == "wash":
        Sipke.play(-3)
exit