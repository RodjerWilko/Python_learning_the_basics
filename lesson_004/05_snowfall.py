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
length_snow = []
list_xy = []
# TODO Удобнее хранить координаты и параметры снежинок в одной структуре данных.
#  Так работать с ними будет проще:
#  snowflakes = [[0, 2, 4], [5, 6, 7], ...]
#  список со списками:
#  for x, y, length in snowflakes:
#      point = Point(x, y)
#      snowflake(point, length)
#  или список со словарями:
#  snowflakes = [{"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, ]
#  for snowflake in snowflakes:
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
#  snowflakes = {1: {"x": 0, "y": 2, "length": 4}, {"x": 5, "y": 6, "length": 7}, }
#  for i, snowflake in snowflakes.items():
#      point = Point(snowflake['x'], snowflake['y'])
#      snowflake(point, snowflake["length"])
for _ in range(N):
    length_snow.append(sd.random_number(10, 100))
for _ in range(N):
    list_xy.append([sd.random_number(0, 800), sd.random_number(600, 800)])

while True:
    # TODO Лучше делать цикл по списку с параметрами снежинок.
    #  В этом цикле нужен индекс элемента, поэтому можно применить
    #  enumerate для списка или ключ словаря.
    #  Объявление цикла будет немного сложнее, но можно будет существенно
    #  упростить остальной код.
    #  Пример для списка:
    #  for i, (x, y, length) in enumerate(snowflake_param):
    #  Пример для словаря, содержащего список параметров снежинки:
    #  for i, (x, y, length) in snowflake_param.items():
    #  Индекс i понадобится для обновления высоты и замены упавшей снежинки.
    for i in range(N):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(*list_xy[i]), length=length_snow[i], color=sd.background_color)
        list_xy[i][1] -= 10
        sd.snowflake(center=sd.get_point(*list_xy[i]), length=length_snow[i], color=sd.COLOR_WHITE)
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break

sd.pause()

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
    for n, coord in enumerate(list_xy):
        sd.start_drawing()
        sd.snowflake(center=sd.get_point(*coord), length=length_snow[n], color=sd.background_color)
        coord[1] -= 10
        coord[0] += sd.random_number(-50, 50)
        sd.snowflake(center=sd.get_point(*coord), length=length_snow[n], color=sd.COLOR_WHITE)
        if coord[1] < length_snow[n]:
            list_xy.append([sd.random_number(0, 800), sd.random_number(600, 2000)])
            length_snow.append(sd.random_number(10, 100))
            continue


        sd.finish_drawing()
        sd.sleep(0.01)
        # TODO Этот код нужно вынести из внутреннего цикла, убрав лишние отступы.
        if sd.user_want_exit():
            break
sd.pause()
