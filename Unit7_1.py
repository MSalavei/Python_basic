class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        s=""
        for i in range(len(self.lst)):
            for j in range(len(self.lst[i])):
                s += f"{self.lst[i][j]:02}  "
            s += "\n"
        return s

    def __add__(self, other):
        lst = [[self.lst[i][j]+other.lst[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))]
        return Matrix(lst)

a = Matrix([[1, 2,3], [4, 5, 6], [1, 7, 9]])
b = Matrix([[11, 12, 13], [14, 15, 16], [11, 17, 19]])
print(a)
print(b)
print(a+b)