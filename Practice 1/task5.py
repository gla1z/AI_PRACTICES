import random as rd

names = ("Володя", "Егорик", "Влад А4", "Глент", "Ботинок")
classes = ("Воин", "Пророк", "Герой", "Заключённый", "Бродяга", "Бандит", "Самурай", "Астролог", "Духовник", "Мерзавец")
characters = ["Жизненная сила", "Интеллект", "Стойкость", "Сила", "Ловкость", "Мудрость", "Вера", "Колдовство"]
parameters = ("Любит клещей", "Боится воды", "Ни для без майнкрафта", "Всегда говорит", "Не открывает глаза", "Хочет стать сайтамой")
points = 24

print("Генератор персонажей")
print(f"Имя персонажа: {rd.choice(names)}")
print(f"Возраст персонажа: {rd.randint(14,99)}")
print(f"Класс персонажа: {rd.choice(classes)}\n")
#print(f"\nХарактеристики персонажа\nЖизненная сила: {rd.randint(0,10)}\nИнтеллект: {rd.randint(0,10)}\nСтойкость: {rd.randint(0,10)}\nСила: {rd.randint(0,10)}\nЛовкость: {rd.randint(0,10)}\nМудрость: {rd.randint(0,10)}\nВера: {rd.randint(0,10)}\nКолдовство: {rd.randint(0,10)}")
print("Характеристики персонажа")
for i in characters:
    if points >= 0:
        ch = rd.randint(0,points)
    print(f"{i} - {ch}")
    points -= ch
print(f"Особенность персонажа: {rd.choice(parameters)}")