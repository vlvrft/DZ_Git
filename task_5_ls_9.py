class Stationery:
    def __init__(self, title="create something"):
        self.title = title

    def draw(self):
        print(f'Just start {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'{self.title} a pen')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}  a pencil')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}')


stat = Stationery()
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Kores')
pencil.draw()
handle = Handle('Copic')
handle.draw()
