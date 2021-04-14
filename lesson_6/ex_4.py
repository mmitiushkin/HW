class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self._direction = ''

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        if self.speed == 0:
            print(f"Нельзя повернуть на {direction} пока стоим")
            return
        self._direction = direction

    def show_speed(self):
        print(f'Скорость = {self.speed} км/ч')
        if hasattr(self, '_max_speed') and self.speed > self._max_speed:
            print(f'Вы превысили скорость на {self.speed - self._max_speed} км/ч')

    @property
    def direction(self):
        return self._direction


class TownCar(Car):
    _max_speed = 60


class SportCar(Car):
    pass


class WorkCar(Car):
    _max_speed = 40


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


car = Car(100, 'blue', 'Nippan', False)
tc = TownCar(70, 'red', 'Lesus', False)
sc = SportCar(60, 'red', 'landorbini', False)
wc = WorkCar(30, 'red', 'Lada', False)


print(tc.show_speed())
tc.turn("left")
print(tc.direction)
tc.turn("right")
print(tc.direction)
print(wc.show_speed())
