class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Машина поехала!")

    def stop(self):
        print("Машина остановилась!")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость машины: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Текущая скорость машины: {self.speed} км/ч")
        if self.speed > 60:
            print("Превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Текущая скорость машины: {self.speed} км/ч")
        if self.speed > 40:
            print("Превышение скорости")


class PoliceCar(Car):
    pass


a = TownCar(90, "green", "Jeep", False)
a.go()
a.turn("направо")
a.show_speed()
b = WorkCar(60, "red", "Zil", False)
b.go()
b.turn("налево")
b.show_speed()