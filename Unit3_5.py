sum = 0
br = 0
while br != 1:
    b = []
    b = [i for i in input('Введите значения чисел через пробел.  Для прекращения работы программы введите х: ').split()]
    for i, el in enumerate(b):
        if el != 'х':
            sum += int(el)
        else:
            br = 1
            break
    print(f"Текущая сумма равна {sum}")
print(f"Программа завершена. Итоговая сумма равна {sum}")