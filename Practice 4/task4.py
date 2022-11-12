class KgToPounds:
    def __init__(self, kg):
        self.__kg = kg

    def to_pounds(self):
        return self.__kg * 2.205

    def set_kg(self, new_kg):
        if isinstance(new_kg, (int, float)):
            self.__kg = new_kg
        else:
            try:
                if "." in new_kg:
                    new_kg = float(new_kg)
                else:
                    new_kg = int(new_kg)
                self.__kg = new_kg
            except:
                raise ValueError("Киллограммы задаются только числами")

    def get_kg(self):
        return self.__kg

    kg = property(get_kg, set_kg)

while True:
    __kg = input("Введите кг, для остановки напишите '0'\n")
    if __kg == '0':
        break
    pr = KgToPounds(__kg)
    pr.kg = __kg
    print("\nНа данный момент, находится:", pr.kg)
    print("Переведены в фунты: ", pr.to_pounds(),"\n")