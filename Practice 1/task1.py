print("Введите 2 переменные")
a = int(input("Введите переменную [a]: "))
b = int(input("Введите переменную [b]: "))

print(
    "\n[1] Сложение\n[2] Вычитание\n[3] Умножение\n[4] Деление\n[5] Возведение в степень\n[6] Остаток от деления\n[7] Извлечение корня\n")
operation = input('Введите номер операции: ')

if operation == '1':
    print("Ответ:", a + b, '\n')
if operation == '2':
    print("Ответ:", a - b, '\n')
if operation == '3':
    print("Ответ:", a * b, '\n')
if operation == '4':
    print("Ответ:", a / b, '\n')
if operation == '5':
    print("Ответ:", a ** b, '\n')
if operation == '6':
    print("Ответ:", a % b, '\n')
if operation == '7':
    print("Ответ:", a ** (1/b), '\n')
if operation >= '8':
    print("[Error] Такой операции не существует в этом калькуляторе :(")