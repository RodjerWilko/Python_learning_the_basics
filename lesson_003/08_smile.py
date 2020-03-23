# -*- coding: utf-8 -*-

# (определение функций)
import random

import simple_draw as sd


# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(_x, _y, color):
    """Функция рисуюет смайл"""
    center_position = sd.Point(_x, _y)
    center_position_left_eye = sd.Point(_x - 15, _y + 15)
    center_position_right_eye = sd.Point(_x + 15, _y + 15)
    first_dot_smile = sd.Point(_x - 25, _y - 10)
    second_dot_smile = sd.Point(_x - 5, _y - 20)
    third_dot_smile = sd.Point(_x + 5, _y - 20)
    four_dot_smile = sd.Point(_x + 25, _y - 10)
    point_list = [first_dot_smile, second_dot_smile, third_dot_smile, four_dot_smile]
    radius = 50
    radius_eye = 5
    sd.circle(center_position=center_position, radius=radius, color=color, width=4)
    sd.circle(center_position=center_position_left_eye, radius=radius_eye, color=color, width=3)
    sd.circle(center_position=center_position_right_eye, radius=radius_eye, color=color, width=3)
    sd.lines(point_list=point_list, color=color, width=3)


for _ in range(10):
    x = random.randint(0, 600)
    y = random.randint(0, 600)
    smile(x, y, sd.COLOR_BLACK)

sd.pause()
