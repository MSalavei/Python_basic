# Unit4_2

from random import randint
my_list = []
my_new_list = []
k = 1
while k < 20:
    my_list.append(randint(1, 1000))
    k += 1
print(f"Исходный список: {my_list}")
for i in range (1, len(my_list)):
    if my_list[i] > my_list[i-1]:
        my_new_list.append(my_list[i])
print(f"Итоговый список: {my_new_list}")