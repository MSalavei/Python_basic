my_list = [7, 5, 3, 3, 2]
a = int(input('Введите  натуральное число: '))
if my_list.count(a) != 0:
    my_list.insert(my_list.index(a), a)
else:
    my_list.append(a)
my_list.sort(reverse=True)
print(my_list)