# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


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


COLOR = [
    {'name_color': 'red', 'code_color': sd.COLOR_RED},
    {'name_color': 'orange', 'code_color': sd.COLOR_ORANGE},
    {'name_color': 'yellow', 'code_color': sd.COLOR_YELLOW},
    {'name_color': 'green', 'code_color': sd.COLOR_GREEN},
    {'name_color': 'cyan', 'code_color': sd.COLOR_CYAN},
    {'name_color': 'blue', 'code_color': sd.COLOR_BLUE},
    {'name_color': 'purple', 'code_color': sd.COLOR_PURPLE}
]

FIGURE = [
    {'name_figure': 'треугольник'},
    {'name_figure': 'квадрат'},
    {'name_figure': 'пятигольник'},
    {'name_figure': 'шестигольник'},
]
# TODO Будет удобнее создать словарь в значениях которого будут храниться
#  названием фигур и ссылками на функции, а ключами словаря будут цифры,
#  вводимые пользователем.
#  Ссылки на функции, проще говоря их названия, можно поместить в структуру данных:
#  список, кортеж, словарь, ... На примере списков это работает так:
#  functs = [pentagon, hexagon, triangle]
#  draw_function = functs[0]
#  draw_function(start_point, start_angle, length
print('Возможные цвета: ')
for i in range(7):
    print("  ", i, ':', COLOR[i]['name_color'])
while True:
    input_user = int(input('Введите желаемый цвет > '))
    if input_user > 6 or input_user < 0:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break
print('Возможные фигуры: ')
for i in range(4):
    print("  ", i, ':', FIGURE[i]['name_figure'])
while True:
    input_user2 = int(input('Введите желаемую фигуру > '))
    if input_user2 > 3 or input_user2 < 0:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break
if input_user2 == 0:
    draw_triangle(_start_point=sd.get_point(100, 100), _angle=20, _length=100,
                  _color=COLOR[input_user]['code_color'])
elif input_user2 == 1:
    draw_box(_start_point=sd.get_point(300, 300), _angle=40, _length=100,
             _color=COLOR[input_user]['code_color'])
elif input_user2 == 2:
    draw_pentagon(_start_point=sd.get_point(100, 400), _angle=30, _length=100,
                  _color=COLOR[input_user]['code_color'])
elif input_user2 == 3:
    draw_hexagon(_start_point=sd.get_point(400, 100), _angle=30, _length=100,
                 _color=COLOR[input_user]['code_color'])
sd.pause()
