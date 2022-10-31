t = int(input("Введите время: "))
a = int(input("Введите ускорение тела: "))

def function(a, t, x0=0, v=60):
    x = x0 + v * t + ((a * (t**2)) / 2)
    return x

print("Вывод: x =", function(a, t))