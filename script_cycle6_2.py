from sys import argv
from itertools import cycle

script_name = argv
i = 1
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for el in cycle(my_list):
    if i > 15:
        break
    print(el)
    i += 1
