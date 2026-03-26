# Activity 1

class pet:
    def __init__(self, name, happiness):
        self.name = name
        self.__happiness = happiness

    def play(self, moraleincreasement):
        self.__happiness += moraleincreasement

    def show_status(self):
        print(self.__happiness)

Sipke = pet("Sipke", 5)

