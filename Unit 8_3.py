class Error_finding:


    @staticmethod
    def is_number(str):
        try:
            float(str)
            return True
        except:
            print("Это было не число! Я не добавлю его в список!")
            return False

ls=[]
while True:
    s=input("Введите очередное число (для выхода введите stop): ")
    if Error_finding.is_number (s) == True:
        ls.append(float(s))
    if s == "stop":
        break
print(f"Список введенных чисел: {ls}")