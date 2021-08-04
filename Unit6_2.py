# Unit6_2

class Road:
    def __init__(self, length, width):
        self._width = width
        self._length = length
        mass = self._width * self._length * 25 * 5
        print(f"Масса асфальта, необходимая для покрытия всего дорожного полотна, равна {mass / 1000} т")


a = Road(20, 5000)