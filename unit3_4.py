a = float(input("Введите действительное положительное число: "))
b = int(input("Введите целое отрицательное число: "))


def my_func(x, y):
    ans1 = round(x ** y, 3)
    ans2 = 1 / x
    for i in range(1, abs(y)):
        ans2 = ans2*1/x
    ans2 = round(ans2, 3)
    return print(f"Возведение в отрицательную степень первым способом: {ans1}, вторым способом {ans2}")


my_func(a, b)