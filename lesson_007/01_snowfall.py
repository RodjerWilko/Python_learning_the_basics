# -*- coding: utf-8 -*-

import simple_draw as sd


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 800)
        self.y = sd.random_number(500, 600)
        self.length = sd.random_number(10, 35)

    def clear_previous_picture(self):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length,
                     color=sd.background_color)
        sd.finish_drawing()

    def move(self):
        self.y -= 15

    def draw(self, color):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(self.x, self.y), length=self.length,
                     color=color)
        sd.finish_drawing()

    def can_fall(self):
        if self.y > 0:
            return True


# flake = Snowflake()

# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw(color=sd.COLOR_DARK_RED)
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:

def get_flakes(count):
    _flakes = []
    for i in range(count):
        _flakes.append(Snowflake())
    return _flakes


def get_fallen_flakes(_flakes):
    _fallen_flakes = []
    for i, _flake in enumerate(_flakes):
        if not _flake.can_fall():
            _fallen_flakes.append([i, _flake])
    return _fallen_flakes


def append_flakes(count):
    for i in count[::-1]:
        del flakes[i[0]]

    flakes.extend(get_flakes(count=len(count)))


N = 20

flakes = get_flakes(count=N)  # создать список снежинок

while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw(color=sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes(flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
