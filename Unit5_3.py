with open("test5_3.txt", "r") as file_obj:
    sum = 0
    print ("Фамилии сотрудников с окладом менее 20.0000:")
    content = file_obj.read().split("\n")
    for i in range(len(content)):
        sum += float(content[i].split(" ")[1])
        if float(content[i].split(" ")[1]) < 20000:
            print(content[i].split(" ")[0])
    print(f"Средняя величина дохода сотрудников равна {round (sum/len(content), 2)} рублей")