# Unit4_4

from random import randint
my_list = []
my_new_list = []
k = 1
while k <100:
    my_list.append(randint(1, 100))
    k += 1
print(f"Исходный список: {my_list}")
my_new_list = [el for el in my_list if my_list.count(el) == 1]
print(f"Итоговый список: {my_new_list}")