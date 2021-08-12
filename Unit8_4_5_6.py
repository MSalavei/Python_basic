class TechnicStore:
    count = 1
    dict_storage = {}
    dict_company = {}
    count_company = 1

    def store_in(self):
        print(f"На склад можно отправить следующие товары: {OrgTechnic.dict}")
        while True:
            idn_store = int(input("Введите идентификационный номер товара, который необходимо сохранить на складе: (для выхода введите 0): "))
            if idn_store in OrgTechnic.dict.keys():
                self.dict_storage[self.count] = OrgTechnic.dict[idn_store]
                self.count+=1
            else:
                print("Товара с таким idn не найдено!")
            if idn_store == 0:
                break
        print(f"Теперь на складе имеются следующие товары: {self.dict_storage}")

    def store_out (self):
        print(f"Вы можете получить следующие товары: {self.dict_storage}")
        while True:
            i = int(input("Введите порядковый номер товара, который необходимо отдать компании: (для выхода введите 0): "))
            if i in self.dict_storage.keys():
                self.dict_company[self.count_company] = self.dict_storage[i]
                del self.dict_storage[i]
                self.count_company += 1
            else:
                print("Товара с таким номером не найдено!")
            if i == 0:
                break
        print(f"Теперь на складе остались следующие товары: {self.dict_storage}")
        print (f"А в компанию переданы следующие позиции: {self.dict_company}")

class OrgTechnic:
    dict = {}
    ls = []
    def __init__(self):
        self.idn = "" # инвентарный номер устройства
        self.type = "" # тип устройства (p- принтер, х - ксерокс, s - сканер)
        self.model = "" # модель устройства
        self.quantity = 0 # количество экземпляров
        self.price = 0 # цена за 1 единицу
        self.other = "" # уникальный для каждого устройства параметр

    def device_creation(self, idn, type, model, quantity, price, other):
        Validation.valid_method(idn)
        Validation.valid_method(quantity)
        Validation.valid_method(price)
        self.ls = [type, model, quantity, price, other]
        self.dict[idn] = self.ls
        print("Объект создан!")


class Printer (OrgTechnic):
    def __init__(self, idn, type, model, quantity, price, color):
        super().__init__()
        self.color = color
        self.device_creation(idn, type, model, quantity, price, color)


class Xerox(OrgTechnic):
    def __init__(self, idn, type, model, quantity, price, assignment):
        super().__init__()
        self.assignment = assignment
        self.device_creation(idn, type, model, quantity, price, assignment)


class Scanner(OrgTechnic):
    def __init__(self, idn, type, model, quantity, price, scanning_speed):
        super().__init__()
        self.scanning_speed = scanning_speed
        self.device_creation(idn, type, model, quantity, price, scanning_speed)

class Validation:
    @staticmethod
    def valid_method(obj):
        try:
            float(obj)
            return True
        except ValueError:
            print (f"{obj} имеет не числовое значение!")
            return False


a = Scanner(108, "s", "scanner 234", "fsf", 200, "12/min")
b = Xerox(100, "x", "xerox 125", 6, 500, "h")
c = Printer(105, "p", "epson 124", 10, 150, "m")
s = TechnicStore()
s.store_in()
s.store_out()