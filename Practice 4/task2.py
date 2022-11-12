class Nikola:
    __slots__ = ['name', 'age']

    def __init__(self, name="", age=""):
        self.name = name
        self.age = age

    def add_name(self):
        self.name = input("Введите имя: ")
        self.age = input("Введите возраст: ")

    def its_me(self):
        if self.name == "Николай" or self.name == "николай":
            print("Да,я", self.name, "\nМне",self.age, "лет :)")
        else:
            print("Я не", self.name, "\nЯ Николай и мне", self.age, "лет :(")

name = Nikola()
name.add_name()
name.its_me()