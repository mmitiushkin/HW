class Cell:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return self.amount + other.amount

    def __sub__(self, other):
        if self.amount - other.amount > 0:
            return self.amount - other.amount
        else:
            return 'No'

    def __mul__(self, other):
        if self.amount > other.amount:
            return Cell(self.amount * other.amount)
        else:
            return 'Error'

    def __str__(self):
        return str(self.amount)

    def __truediv__(self, other):
        if self.amount > other.amount:
            return Cell(round(self.amount / other.amount))
        else:
            return 'Error'

    def make_order(self, some):
        a = self.amount // some
        b = self.amount % some
        string = '*' * some + '\n'
        string2 = '*' * b + '\n'
        return string * a + string2


c1 = Cell(8)
c2 = Cell(50)

print(c1+c2)
print(c2-c1)

print(c2*c1)
print(c2/c1)

print((c2*c1).make_order(50))
# print((c2/c1).make_order(5))

print(c1.make_order(5))
