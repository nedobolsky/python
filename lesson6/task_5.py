class Stationery:
    def __init__(self, title="Начинайте рисовать"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки. {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Рисование ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисование карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'Рисование маркером')


static = Stationery()
static.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
