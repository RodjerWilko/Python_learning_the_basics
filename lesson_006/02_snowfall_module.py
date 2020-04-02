# -*- coding: utf-8 -*-

import simple_draw as sd

import snowfall as sw

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall


N = 35

sw.create_snowflake(N)

while True:
    sw.draw_snowflakes_color(color=sd.background_color)
    sw.move_snowflakes()
    sw.draw_snowflakes_color(color=sd.COLOR_YELLOW)
    my_list = sw.numbers_down()
    if my_list:
        sw.del_snowflakes(my_list)
        sw.create_snowflake(len(my_list))
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
