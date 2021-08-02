import random
sum=0
with open("test5_5.txt", "w+") as file_obj:
        for i in range (30):
                file_obj.write(str(random.randint(0, 100))+" ")
        file_obj.seek(0)
        content = list(file_obj.read().split())
        for i in range (len(content)):
                sum+=int(content[i])
        print(f"Сумма чисел в файле: {sum}")