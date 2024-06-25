class Buiding:
    total = 0

    def __init__(self):
        Buiding.total += 1


i = 0
while i < 40:
    buiding = Buiding()
    print(buiding.total)
    i += 1
