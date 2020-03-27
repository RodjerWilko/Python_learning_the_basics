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


def draw_figure(_sides, _start_point, _angle, _length, _angle_k, _color):
    _end_point = _start_point
    for _ in range(_sides):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw(color=_color)
        _angle = _angle + _angle_k
        _start_point = v.end_point
    sd.line(start_point=_start_point, end_point=_end_point, color=_color)


def draw_triangle(_start_point, _angle, _length, _color):
    draw_figure(_sides=3, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=120, _color=_color)


def draw_box(_start_point, _angle, _length, _color):
    draw_figure(_sides=4, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=90, _color=_color)


def draw_pentagon(_start_point, _angle, _length, _color):
    draw_figure(_sides=5, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=72, _color=_color)


def draw_hexagon(_start_point, _angle, _length, _color):
    draw_figure(_sides=6, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=60, _color=_color)


COLOR = {
    0: {'name_color': 'red', 'code_color': sd.COLOR_RED},
    1: {'name_color': 'orange', 'code_color': sd.COLOR_ORANGE},
    2: {'name_color': 'yellow', 'code_color': sd.COLOR_YELLOW},
    3: {'name_color': 'green', 'code_color': sd.COLOR_GREEN},
    4: {'name_color': 'cyan', 'code_color': sd.COLOR_CYAN},
    5: {'name_color': 'blue', 'code_color': sd.COLOR_BLUE},
    6: {'name_color': 'purple', 'code_color': sd.COLOR_PURPLE}
}

print('Возможные цвета:')
for i in COLOR:
    print("  ", i, ':', COLOR[i]['name_color'])
while True:
    input_user = int(input('Введите желаемый цвет > '))
    if input_user not in COLOR:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break

draw_triangle(_start_point=sd.get_point(100, 100), _angle=20, _length=100, _color=COLOR[input_user]['code_color'])
draw_box(_start_point=sd.get_point(300, 300), _angle=40, _length=100, _color=COLOR[input_user]['code_color'])
draw_pentagon(_start_point=sd.get_point(100, 400), _angle=30, _length=100, _color=COLOR[input_user]['code_color'])
draw_hexagon(_start_point=sd.get_point(400, 100), _angle=30, _length=100, _color=COLOR[input_user]['code_color'])

sd.pause()

# зачет!
