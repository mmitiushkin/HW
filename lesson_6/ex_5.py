class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):
    def draw(self):
        print('Это пишет ручка.')


class Pencil(Stationary):
    def draw(self):
        print('Это пишет карандаш.')


class Handle(Stationary):
    def draw(self):
        print('Это пишет маркер.')


pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

pen.draw()
pencil.draw()
handle.draw()
