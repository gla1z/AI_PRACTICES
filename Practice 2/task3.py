n = int(input("Введите число: "))

sum = 0
while n > 0:
    last_num = n % 10
    n //= 10
    sum += last_num
print("Сумма всех цифр:", sum)