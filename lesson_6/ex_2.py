class Road:
    weight = 25       # кг
    thickness = 0.05  # м
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc(self):
        return self._length * self._width * self.weight * self.thickness


road = Road(20, 5000)
print(road.calc())
