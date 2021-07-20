l= []
n = int(input("Введите количество элементов листа:"))
print(f"Введите {n} элементов листа, нажимая после каждого элемента списка Enter:")
for i in range(0, n):
    l.append(input())
if n % 2 != 0:
    n -= 1
for i in range(0, n - 1, 2):
    m = l[i + 1]
    l[i + 1] = l[i]
    l[i] = m
print(l)