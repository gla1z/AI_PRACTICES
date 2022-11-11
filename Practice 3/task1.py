from random import randint

def func_try():
    try:
        return 10/randint(0,1)
    except ZeroDivisionError:
        return "Деление на 0"

print(func_try())