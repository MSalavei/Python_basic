s = input('Введите строку: ')
l = []
l = s.split(' ')
i = 1
for el in l:
    print(str(i) + '.' + el[:10])
    i += 1