# Unit4_5

from functools import reduce
my_list = [el for el in range(100, 1001, 2)]
result = reduce(lambda x, y: x*y, my_list)
print(result)