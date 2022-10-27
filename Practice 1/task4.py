import time
<<<<<<< HEAD
try:
    timer_value = time.strptime(input("Введите время в формате ЧЧ:ММ:СС\n"), '%H:%M:%S')
except:
    print("Время введено не по формату")
timer_end = time.time() + 3600 * timer_value.tm_hour + 60 * timer_value.tm_min + timer_value.tm_sec
while time.time() <= timer_end:
    print(time.strftime('%H:%M:%S', time.gmtime(timer_end - time.time())))
    time.sleep(1)
print("Пора отдыхать!")
=======

timer = time.strptime(input("Введите время в формате ЧЧ:ММ:СС\n"), '%H:%M:%S')
timer_end = time.time() + 3600 * timer.tm_hour + 60 * timer.tm_min + timer.tm_sec
while time.time() < timer_end:
    print(time.strftime('%H:%M:%S', time.gmtime(timer_end - time.time())))
    time.sleep(1)
print("Пора отдыхать!")
>>>>>>> ffb5aff5b9a56cc7451840df3829a071574b8798
