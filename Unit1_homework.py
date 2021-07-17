# Task 1-1.

a = "На календаре сейчас"
b = 2021
c = 'год'
print(a, b, c)

name = input("Введите Ваше имя: ")
birth_year = int(input("Введите Ваш год рождения в формате ХХХХ: "))
d = b-birth_year
print("Ваше имя ", name)
print("Ваш год рождения ", birth_year)
print("Соответственно, Вам ", d)

# Task 1-2

a = int(input("Введите время в секундах: "))
hours = a // 3600
min = (a - hours * 3600) // 60
sec = a - hours * 3600 - min * 60
print(f"Время в формате чч:мм:сс {hours}:{min}:{sec}")

# Task 1-3

a = input("Введите число n:")
sum_n = int(a) + int(a+a) + int(a+a+a)
print("Cумма равна: ", sum_n)

# Task 1-4

a = int(input("Введите целое число: "))
a = abs(a)
baseline_n = a
max_n = 0
i = 1
while i == 1:
    if baseline_n < 10:
        i = 0
    last_n = baseline_n % 10
    if last_n > max_n:
        max_n = last_n
    baseline_n = (baseline_n - last_n) // 10
print(max_n)

# Task 1-5

a = float(input("Введите значение выручки фирмы: "))
b = float(input("Введие значение издержек фирмы: "))
if a > b:
    print("Фирма работает с прибылью!")
    rent = round((a / b), 3)
    c = int(input("Введите количество сотрудников фирмы: "))
    income_per_person = round((a-b) / c, 3)
    print(f"Рентабельность выручки равна {rent}, а прибыль фирмы в расчете на одного сотрудника {income_per_person}")
elif a < b:
    print("Фирма работает с издержками!")
else:
    print("Прибыль и издержки фирмы равны!")

# Task 1-6

a = float(input("Введите результат пробежки в километрах в первый день: "))
b = float(input("Введите целевое значение дистанции пробежки в км: "))
tot_length = a
i = 1
while tot_length <=b:
    tot_length += tot_length*0.1
    i += 1
print("Спортсмен достигнет своей целевой дистанции на ", i, "день")