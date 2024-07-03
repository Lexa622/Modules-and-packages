class Horse:
    """Horse - класс описывающий лошадь."""
    def __init__(self, x_distance=0, sound="Frrr"):
        self.x_distance = x_distance    # пройденный путь.
        self.sound = sound  # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx   # изменение дистанции, увеличивает x_distance на dx.


class Eagle:
    """класс описывающий орла."""
    def __init__(self, y_distance=0, sound='I train, eat, sleep, and repeat'):
        self.y_distance = y_distance    # высота полёта.
        self.sound = sound  # звук, который издаёт орёл (отсылка(Я тренируюсь, ем, сплю и повторяю))

    def fly(self, dy):
        self.y_distance += dy   # изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Horse, Eagle):
    """класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
    Объект такого класса должен обладать атрибутами классов родителей в порядке наследования."""
    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()