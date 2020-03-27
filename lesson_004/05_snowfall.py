# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

sd.resolution = (800, 600)


def new_snowflake():
    _x = sd.random_number(0, 800)
    _y = sd.random_number(700, 800)
    _length = sd.random_number(10, 100)
    _my_dict = {'x': _x, 'y': _y, 'length': _length}
    snowflakes[i] = _my_dict


snowflakes = {}

for i in range(N):
    new_snowflake()

# while True:
#     sd.start_drawing()
#     for i, snowflake in snowflakes.items():
#
#         sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
#                      color=sd.background_color)
#         snowflake['y'] -= 20
#         sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
#                      color=sd.COLOR_WHITE)
#     sd.finish_drawing()
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
#
# sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

while True:
    sd.start_drawing()
    for i, snowflake in snowflakes.items():

        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
                     color=sd.background_color)
        snowflake['y'] -= 10
        snowflake['x'] += sd.random_number(-50, 50)
        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
                     color=sd.COLOR_WHITE)
        if snowflake['y'] < snowflake['length']:
            new_snowflake()
            continue
        sd.sleep(0.005)

    sd.finish_drawing()
    if sd.user_want_exit():
        break
sd.pause()
