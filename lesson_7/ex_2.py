from abc import ABC, abstractmethod


class Clothes(ABC):
    _clothes = []

    def __init__(self, name, size=None, height=None):
        self.name = name
        self.size = size
        self.height = height
        self._clothes.append(self)
        self.tissue = None

    @abstractmethod
    def get_consumption(self):
        pass

    def get_cost(self):
        return self.size

    @property
    def clothes(self):
        return self._clothes

    @property
    def total_tissue(self):
        return f'Общая стоимость ткани: {sum([item.tissue for item in self._clothes])}'


class Coat(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def get_consumption(self):
        self.tissue = self.size / 6.5 + 0.5
        return f'Размер пальто: {self.tissue}'

    def __str__(self):
        return self.name


class Costume(Clothes):
    def __init__(self, name, height):
        super().__init__(name)
        self.height = height

    def get_consumption(self):
        self.tissue = 2 * self.height + 0.3
        return f'Размер костюма: {self.tissue}'

    def __str__(self):
        return self.name


coat = Coat('Пальто', 65)
costume = Costume('Костюм', 45)

print(coat)
print(costume)

print(coat.size)
print(costume.height)

print(coat.get_consumption())
print(costume.get_consumption())

print(coat.total_tissue)
