# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
x = [50, 50]
y = [350, 450]
# TODO Можно сразу назвать переменную color вместо i.
for i in rainbow_colors:
    start_point = sd.Point(x[0], x[1])
    end_point = sd.Point(y[0], y[1])
    x[0] += 5
    y[0] += 5
    color = i
    sd.line(start_point=start_point, end_point=end_point, color=color, width=4)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

center_position = sd.Point(450, 20)
radius = 400


for color in rainbow_colors:
    radius += 20
    sd.circle(center_position=center_position, radius=radius, color=color, width=20)
sd.pause()
