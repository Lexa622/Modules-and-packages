from nim_engine import get_bunches, put_stones, is_game_over, take_from_bunch
from termcolor import cprint, colored


put_stones()
user_namber = 1
while True:
    cprint("Текущая позиция", color="green")
    cprint(get_bunches(), color="green")
    user_color = 'blue' if user_namber == 1 else 'yellow'
    cprint("Ход игрока {}".format(user_namber), color=user_color)
    pos = input(colored("Откуда берём? ", color=user_color))
    qua = input(colored("Сколько берём? ", color=user_color))
    take_from_bunch(position=int(pos), quantity=int(qua))
    if is_game_over():
        break
    user_namber = 2 if user_namber == 1 else 1

print("Выиграл игрок", user_namber)
