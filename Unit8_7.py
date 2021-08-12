class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.a * other.b+other.a*self.b} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'

a1 = int(input("Введите действительную часть 1-ого комплексного числа: "))
b1 = int(input("Введите мнимую часть 1-ого комплексного числа: "))
a2 = int(input("Введите действительную часть 2-ого комплексного числа: "))
b2 = int(input("Введите мнимую часть 2-ого комплексного числа: "))
z_1 = ComplexNumber(a1, b1)
z_2 = ComplexNumber(a2, b2)
print(z_1 + z_2)
print(z_1 * z_2)