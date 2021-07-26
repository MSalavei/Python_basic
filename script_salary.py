from sys import argv

script_name, hours, rate_in_hours, bonus = argv


salary = int(hours) * int(rate_in_hours) + int(bonus)
print("Заработная плата равна: ", salary)
