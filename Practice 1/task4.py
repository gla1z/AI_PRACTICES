import time

timer = time.strptime(input("Введите время в формате ЧЧ:ММ:СС\n"), '%H:%M:%S')
timer_end = time.time() + 3600 * timer.tm_hour + 60 * timer.tm_min + timer.tm_sec
while time.time() < timer_end:
    print(time.strftime('%H:%M:%S', time.gmtime(timer_end - time.time())))
    time.sleep(1)
print("Пора отдыхать!")
