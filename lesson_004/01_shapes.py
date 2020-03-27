# -*- coding: utf-8 -*-

import simple_draw as sd


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

#
# def draw_triangle(_start_point, _angle, _length):
#     for _ in range(3):
#         v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
#         v.draw()
#         _angle = _angle + 120
#         _start_point = v.end_point
#
#
# def draw_box(_start_point, _angle, _length):
#     for _ in range(4):
#         v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
#         v.draw()
#         _angle = _angle + 90
#         _start_point = v.end_point
#
#
# def draw_pentagon(_start_point, _angle, _length):
#     for _ in range(5):
#         v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
#         v.draw()
#         _angle = _angle + 72
#         _start_point = v.end_point
#
#
# def draw_hexagon(_start_point, _angle, _length):
#     for _ in range(6):
#         v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
#         v.draw()
#         _angle = _angle + 60
#         _start_point = v.end_point


# start_point = sd.get_point(100, 100)
# angle = 20
# length = 100
# draw_triangle(_start_point=start_point, _angle=angle, _length=length)
#
# start_point = sd.get_point(300, 300)
# angle = 40
# length = 100
# draw_box(_start_point=start_point, _angle=angle, _length=length)
#
# start_point = sd.get_point(100, 400)
# angle = 30
# length = 100
# draw_pentagon(_start_point=start_point, _angle=angle, _length=length)
#
# start_point = sd.get_point(400, 100)
# angle = 30
# length = 100
# draw_hexagon(_start_point=start_point, _angle=angle, _length=length)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#

#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


def draw_figure(_sides, _start_point, _angle, _length, _angle_k):
    _end_point = _start_point
    for _ in range(_sides):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw()
        _angle = _angle + _angle_k
        _start_point = v.end_point
    sd.line(start_point=_start_point, end_point=_end_point)


def draw_triangle(_start_point, _angle, _length):
    draw_figure(_sides=3, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=120)


def draw_box(_start_point, _angle, _length):
    draw_figure(_sides=4, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=90)


def draw_pentagon(_start_point, _angle, _length):
    draw_figure(_sides=5, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=72)


def draw_hexagon(_start_point, _angle, _length):
    draw_figure(_sides=6, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=60)


start_point = sd.get_point(100, 100)
angle = 20
length = 100
draw_triangle(_start_point=start_point, _angle=angle, _length=length)

start_point = sd.get_point(300, 300)
angle = 40
length = 100
draw_box(_start_point=start_point, _angle=angle, _length=length)

start_point = sd.get_point(100, 400)
angle = 30
length = 100
draw_pentagon(_start_point=start_point, _angle=angle, _length=length)

start_point = sd.get_point(400, 100)
angle = 30
length = 100
draw_hexagon(_start_point=start_point, _angle=angle, _length=length)

sd.pause()

# зачет!
