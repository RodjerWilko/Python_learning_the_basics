# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(_start_point, _angle, _length, _delta=30):
    if _length < 10:
        return
    v1 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v2 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v1.draw()
    next_point = v1.end_point
    next_point2 = v2.end_point
    next_angle = _angle - _delta
    next_angle2 = _angle + _delta
    next_length = _length * .75
    draw_branches(_start_point=next_point, _angle=next_angle, _length=next_length)
    draw_branches(_start_point=next_point2, _angle=next_angle2, _length=next_length)


root_point = sd.get_point(300, 30)
draw_branches(_start_point=root_point, _angle=90, _length=100)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# TODO Разные функции называются одинаково. Переименуйте одну из них.
def draw_branches(_start_point, _angle, _length):
    _delta = sd.random_number(30, 72)
    rand_length = sd.random_number(75, 90) / 100
    # TODO При ограничении длины в 3 пикселя получается слишком много веток.
    #  сложно дождаться завершения отрисовки. Желательно увеличить это число.
    if _length < 3:
        return
    v1 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v2 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v1.draw()
    next_point = v1.end_point
    next_point2 = v2.end_point
    next_angle = _angle - _delta
    next_angle2 = _angle + _delta
    next_length = _length * rand_length
    draw_branches(_start_point=next_point, _angle=next_angle, _length=next_length)
    draw_branches(_start_point=next_point2, _angle=next_angle2, _length=next_length)


root_point = sd.get_point(300, 30)
draw_branches(_start_point=root_point, _angle=90, _length=100)
sd.pause()
