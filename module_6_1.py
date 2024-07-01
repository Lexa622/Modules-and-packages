class Animal:
    """атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного."""
    def __init__(self, name, alive=True, fed=False):
        self.alive = alive
        self.fed = fed
        self.name = name


class Plant:
    """edible = False(съедобность), name - индивидуальное название каждого растения"""
    def __init__(self, name, edible=False):
        self.edible = edible
        self.name = name


class Mammal(Animal):
    def eat(self, food):
        self.fed = True
        print(f"{self.name} сЪел {food.name}")


class Predator(Animal):
    def eat(self, food):
        self.alive = False
        print(f"{self.name} не стал есть {food.name}")


class Flower(Plant):
    edible = False


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
