class Horse:
    def __init__(self, x_distance=0, sound="Frrr"):
        self.x_distance = x_distance    # пройденный путь.
        self.sound = sound  # звук, который издаёт лошадь.
        super().__init__()

    def run(self, dx):
        self.x_distance += dx   # изменение дистанции, увеличивает x_distance на dx.


class Eagle:
    def __init__(self, y_distance=0, sound="I train, eat, sleep, and repeat"):
        self.y_distance = y_distance    # высота полёта.
        self.sound = sound  # звук, который издаёт орёл (отсылка(Я тренируюсь, ем, сплю и повторяю))

    def fly(self, dy):
        self.y_distance += dy   # изменение дистанции, увеличивает y_distance на dy.


class Pegasus(Horse, Eagle):
    def __init__(self):
        super().__init__()

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
