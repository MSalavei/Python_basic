a = float(input("Введите число 1:"))
b = float(input("Введите число 2:"))
c = float(input("Введите число 3:"))


def my_func(a1, b1, c1):
    l = [a1, b1, c1]
    l.sort(reverse=True)
    return print(l[0] + l[1])


my_func(a, b, c)