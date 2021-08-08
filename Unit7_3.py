class Cell:
    def __init__(self, cell_number):
        self.cell_number = cell_number

    def __add__(self, other):
        return Cell(self.cell_number + other.cell_number)

    def __sub__(self, other):
        if (self.cell_number - other.cell_number) > 0:
            return Cell(self.cell_number - other.cell_number)
        else:
            print("Ошибка вычитания!")

    def __mul__(self, other):
        return Cell(self.cell_number * other.cell_number)

    def __truediv__(self, other):
        return Cell(self.cell_number // other.cell_number)

    def make_order(self, c_in_row):
        row = ''
        for i in range(int(self.cell_number / c_in_row)):
            row += f'{"*" * c_in_row} ' + '\n'
        row += f'{"*" * (self.cell_number % c_in_row)}'
        return row

    def __str__(self):
        return f"{self.cell_number}"


c1 = Cell(25)
print(c1.make_order(8))
c2 = Cell(30)
print(c2.make_order(5))
print(c2 + c1)
print(c1 - c2)
print(c2 * c1)
print(c2 / c1)