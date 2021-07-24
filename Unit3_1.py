a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
while b == 0:
    b = float(input("Ошибка, делить на ноль нельзя! Повторите ввод второго числа"))


def div_func(c, d):
    return round(c / d, 3)


print(f"Результат деления числа {a} на число {b} равно {div_func(a, b)}")