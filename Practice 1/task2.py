import random as r

n_words = list()
v_words = list()

print("[+]Введите глаголы\n"
      "[+]Чтобы прекратить набор напишите 'стоп'")
print("Ввод: ", end='')
s_word = input()
while s_word != "стоп":
    print("Ввод: ", end='')
    v_words.append(s_word)
    s_word = input()

print("\n[+]Введите существительные\n"
      "[+]Чтобы прекратить набор напишите 'стоп'")
print("Ввод: ", end='')
s_word = input()
while s_word != "стоп":
    print("Ввод: ", end='')
    n_words.append(s_word)
    s_word = input()

print("\nПрим.[С-существительное][Г-глагол]\n"
      "Выберите вариант предложения, который вы хотите создать\n"
      "[1] СГС\n[2] ГСС\n[3] ССГ")
operation = input("Введите номер операции: ")

if operation == '1':
    print("\nВы выбрали предложения с СУЩ+ГЛАГ+СУШ")
    amount = int(input("Введите количество предложений: "))
    for i in range(amount):
        print(f"[{i + 1}]", r.choice(n_words), r.choice(v_words), r.choice(n_words))

if operation == '2':
    print("\nВы выбрали предложения с ГЛАГ+СУЩ+СУШ")
    amount = int(input("Введите количество предложений: "))
    for i in range(amount):
        print(f"[{i + 1}]", r.choice(v_words), r.choice(n_words), r.choice(n_words))

if operation == '3':
    print("\nВы выбрали предложения с СУЩ+СУЩ+ГЛАГ")
    amount = int(input("Введите количество предложений: "))
    for i in range(amount):
        print(f"[{i + 1}]", r.choice(n_words), r.choice(n_words), r.choice(v_words))

if operation >= '4':
    print("\n[Error] Вы ввели неправильную операцию :(")