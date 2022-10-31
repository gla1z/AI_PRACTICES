import random as rd

industries = ['Сельское хозяйство', 'Легкая промышленность', 'Тяжелая промышленность группы А', 'Тяжелая промышленность группы Б', 'Военно-промышленный комплекс', 'Наука', 'Химическая промышленность']
resp = int(input('Число республик (не больше 11): '))
republic = ['Литва', 'Хорватия', 'Узбекистан', 'Казахстан', 'Азербайджан', 'Белорусия', 'Туркменистан', 'Венесуэла', 'Чили', 'Гватемала', 'Монголия']
republic_w_name = rd.sample(republic, resp)
print(republic_w_name)
inf = {}

for i in range(len(republic_w_name)):
    values = []
    for j in range(len(republic_w_name)):
        values.append(rd.randint(-1,1))
    inf[republic_w_name[i]] = values
print(inf)

lag = [0,0,0,0,0,0,0]
dev = [0,0,0,0,0,0,0]
bal = [0,0,0,0,0,0,0]

for i in inf:
    for j in range(len(inf[i])):
        if inf[i][j] == -1:
            lag[j] += 1
        elif inf[i][j] == 1:
            dev[j] += 1
        else:
            bal[j] += 1

max_lag = max(lag)
print("Самая отстающая отрасль: ", industries[lag.index(max_lag)])
print("Количество отстающих: ", max_lag)

max_dev = max(dev)
print("Самая развитая отрасль: ", industries[dev.index(max_dev)])

max_bal = max(bal)
print("Самая сбалансированная отрасль: ", industries[bal.index(max_bal)])

stat = [0,0,0,0,0,0,0]
for i in inf:
    result = map(sum, zip(inf[i], stat))
    stat = result
print("Статистика отраслей: ", list(stat))