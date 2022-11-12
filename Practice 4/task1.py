class Soda:
    def __init__(self, add):
        self.add = add

    def show_my_drink(self):
        if len(self.add) != 0:
            print("Газировка с " + self.add)
        else:
            print("Обычная газировка")

gaz = Soda(input("Введите добавку: "))
gaz.show_my_drink()