class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationary):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationary):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationary):
    def draw(self):
        print("Запуск отрисовки маркером")


a = Pen("Pen")
a.draw()
b = Pencil("Pencil")
b.draw()
c = Handle("Handle")
c.draw()