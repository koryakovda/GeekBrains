class Stationery:
    def __init__(self,title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки Pen')
class Pencile(Stationery):
    def draw(self):
        print('Запуск отрисовки Pencile')
class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки Handle')

handle = Handle('Маркер')
handle.draw()
pen = Pen('Ручка')
pen.draw()
pencile = Pencile('Карандаш')
pencile.draw()