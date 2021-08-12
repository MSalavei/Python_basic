# Unit 8_1
class Data:

    @classmethod
    def transorm_method(self, date):
        self.date = date
        a, b, c = self.date.split("-")
        print(self.validation(a, b, c))
        return int(a + b + c)

    @staticmethod
    def validation(a, b, c):
        if int(a) <= 0 or int(a) > 31:
            return "Ошибочно введен день месяца!"
        if int(b) < 0 or int(b) > 12:
            return "Ошибочно введен месяц!"
        if int(c) < 0:
            return "Дело было до нашей эры?"


print (Data.validation(12, 16, -5))
print(f"Преобразованная в число дата: {Data.transorm_method(input('Введите дату в формате ДД-ММ-ГГГГ: '))} ")
