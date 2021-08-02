count_lines = 0
with open("test5_2.txt", 'r') as file_obj:
    for line in file_obj:
        count_lines += 1
        count_words = len(line.split(" "))
        print(f"В строке {count_lines} количество слов: {count_words}")
print(f"Общее количество строк в файле: {count_lines}")