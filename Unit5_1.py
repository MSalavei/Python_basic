# Unit 5_1
with open("test.txt", 'w') as file_obj:
    print("Вводите строки текста. Окончание ввода - пустая строка!")
    while True:
        s = input()
        if s == '':
            break
        print(s, file=file_obj)
