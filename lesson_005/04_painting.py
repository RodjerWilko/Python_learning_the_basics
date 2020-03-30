# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)
import simple_draw as sd

import draw.house
import draw.rainbow
import draw.snowflake
import draw.sun
import draw.tree

sd.resolution = (1400, 750)

draw.rainbow.draw_rainbow()
draw.house.draw_house()
draw.tree.draw_tree(_start_point=sd.get_point(1100, 0), _angle=90, _length=100, _color=sd.COLOR_DARK_CYAN)
draw.sun.draw_sun(_x=150, _y=650, _color=sd.COLOR_DARK_RED)
draw.snowflake.snowflakes(0, 400, 0, 30)

# sd.pause()

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# while True:
#     draw.rainbow.draw_rainbow(_i=0)
#     draw.tree.draw_tree(_start_point=sd.get_point(1100, 0), _angle=90, _length=100, _color=sd.COLOR_DARK_CYAN)
#     draw.sun.draw_sun(_x=150, _y=650, _color=sd.COLOR_YELLOW)
#     draw.rainbow.draw_rainbow(_i=1)
#     draw.sun.draw_sun(_x=150, _y=650, _color=sd.background_color)
#     draw.sun.draw_sun(_x=150, _y=650, _color=sd.COLOR_YELLOW, _step=45)
#     draw.house.draw_house()
#     draw.snowflake.snowflakes(0, 400, 350, 500)


sd.pause()

