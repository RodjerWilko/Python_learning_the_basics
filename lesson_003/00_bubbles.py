# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.Point(100, 200)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(center_position=point, radius=radius)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет
def bubble(point_, radius_, color_,):
    """Функция рисует пузырь"""
    for _ in range(3):
        radius_ += 5
        sd.circle(center_position=point_, radius=radius_, color=color_)


# Нарисовать 10 пузырьков в ряд
radius = 50
color = sd.COLOR_RED
for x in range(100, 1100, 100):
    point = sd.Point(x, 200)
    bubble(point_=point, radius_=radius, color_=color)

# Нарисовать три ряда по 10 пузырьков
radius = 50
color = sd.COLOR_RED
for y in range(100, 310, 100):
    for x in range(100, 1100, 100):
        point = sd.Point(x, y)
        bubble(point_=point, radius_=radius, color_=color)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

radius = 50
for _ in range(100):
    point = sd.Point(random.randint(10, 1000), random.randint(10, 1000))
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    bubble(point_=point, radius_=radius, color_=color)

sd.pause()

# зачет!
