class TriangleChecker:
    def __init__(self, a="", b="", c=""):
        self.a = a
        self.b = b
        self.c = c

    def add_side(self):
        self.a = int(input("Введите первое число: "))
        self.b = int(input("Введите второе число: "))
        self.c = int(input("Введите третье число: "))

    def is_triangle(self):
        if self.a < 0 or self.b < 0 or self.c < 0:
            print("С отрицательными нельзя")
        elif  self.a + self.b >= self.c and self.a + self.c >= self.b and self.b + self.c >= self.a:
            print("Такой треугольник существует")
        else:
            print("Такой треугольник существовать не может")

res = TriangleChecker()
res.add_side()
res.is_triangle()