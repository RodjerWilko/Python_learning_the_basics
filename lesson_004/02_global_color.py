# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def draw_triangle(_start_point, _angle, _length, _color):
    for _ in range(3):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length, )
        v.draw(color=_color)
        _angle = _angle + 120
        _start_point = v.end_point


def draw_box(_start_point, _angle, _length, _color):
    for _ in range(4):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw(color=_color)
        _angle = _angle + 90
        _start_point = v.end_point


def draw_pentagon(_start_point, _angle, _length, _color):
    for _ in range(5):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw(color=_color)
        _angle = _angle + 72
        _start_point = v.end_point


def draw_hexagon(_start_point, _angle, _length, _color):
    for _ in range(6):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw(color=_color)
        _angle = _angle + 60
        _start_point = v.end_point


# TODO Если COLOR сделать словарём, то обрабатывать пользовательский ввод станет проще.
#  Посмотрите пример в задании с днями месяца в 3 уроке.
COLOR = [
    {'name_color': 'red', 'code_color': sd.COLOR_RED},
    {'name_color': 'orange', 'code_color': sd.COLOR_ORANGE},
    {'name_color': 'yellow', 'code_color': sd.COLOR_YELLOW},
    {'name_color': 'green', 'code_color': sd.COLOR_GREEN},
    {'name_color': 'cyan', 'code_color': sd.COLOR_CYAN},
    {'name_color': 'blue', 'code_color': sd.COLOR_BLUE},
    {'name_color': 'purple', 'code_color': sd.COLOR_PURPLE}
]

print('Возможные цвета:')
for i in range(7):
    print("  ", i, ':', COLOR[i]['name_color'])
while True:
    input_user = int(input('Введите желаемый цвет > '))
    if input_user > 6 or input_user < 0:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break

draw_triangle(_start_point=sd.get_point(100, 100), _angle=20, _length=100, _color=COLOR[input_user]['code_color'])
draw_box(_start_point=sd.get_point(300, 300), _angle=40, _length=100, _color=COLOR[input_user]['code_color'])
draw_pentagon(_start_point=sd.get_point(100, 400), _angle=30, _length=100, _color=COLOR[input_user]['code_color'])
draw_hexagon(_start_point=sd.get_point(400, 100), _angle=30, _length=100, _color=COLOR[input_user]['code_color'])

sd.pause()
