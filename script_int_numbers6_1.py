from sys import argv
from itertools import count

script_name, start_n = argv

for el in count(int(start_n)):
    if el > 10:
        break
    else:
        print(el)