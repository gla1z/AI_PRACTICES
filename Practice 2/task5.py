bd = {}

print("Начальный словарь: ", bd)

while input("Ввести данные сотрудника? 1 - да, 0 - нет : ") != '0':
    name = input("Введите ФИО сотрудника: ")
    age = int(input("Введите возраст сотрудника: "))
    job = input("Введите должность работника: ")
    job_num = int(input("Введите номер рабочего места сотрудника: "))
    secret = input("Есть ли у работника доступ к тайне (да/нет): ")
    print('\n')

    bd[name] = {
        "Имя - ", name,
        "Должность - ", job,
        "Номер рабочего места - ", job_num,
        "Наличие доступа к тайне - ", secret
    }