# Unit6_3

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get("wage") + self._income.get("bonus")


a = Position ("Sasha", "Ivanov", "TeamLead", 100000, 20000)
print(f"Полное имя сотрудника: {a.get_full_name()}")
print(f"Суммарный доход: {a.get_total_income()}")