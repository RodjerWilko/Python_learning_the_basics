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


COLOR = {
    0: {'name_color': 'red', 'code_color': sd.COLOR_RED},
    1: {'name_color': 'orange', 'code_color': sd.COLOR_ORANGE},
    2: {'name_color': 'yellow', 'code_color': sd.COLOR_YELLOW},
    3: {'name_color': 'green', 'code_color': sd.COLOR_GREEN},
    4: {'name_color': 'cyan', 'code_color': sd.COLOR_CYAN},
    5: {'name_color': 'blue', 'code_color': sd.COLOR_BLUE},
    6: {'name_color': 'purple', 'code_color': sd.COLOR_PURPLE}
}

FIGURE = {
    0: {'name_figure': 'треугольник', 'func': draw_triangle},
    1: {'name_figure': 'квадрат', 'func': draw_box},
    2: {'name_figure': 'пятигольник', 'func': draw_pentagon},
    3: {'name_figure': 'шестигольник', 'func': draw_hexagon},
}

print('Возможные цвета: ')
for i in COLOR:
    print("  ", i, ':', COLOR[i]['name_color'])
while True:
    input_user = int(input('Введите желаемый цвет > '))
    if input_user not in COLOR:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break
print('Возможные фигуры: ')
for i in FIGURE:
    print("  ", i, ':', FIGURE[i]['name_figure'])
while True:
    input_user2 = int(input('Введите желаемую фигуру > '))
    if input_user2 not in FIGURE:
        print('Вы ввели некорректный номер!')
        continue
    else:
        break

draw_func = FIGURE[input_user2]['func']
draw_func(_start_point=sd.get_point(100, 100), _angle=20, _length=100,
          _color=COLOR[input_user]['code_color'])

sd.pause()

# зачет!
