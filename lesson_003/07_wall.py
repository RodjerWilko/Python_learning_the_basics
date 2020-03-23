# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


count = 1
for i in range(0, 1000, 50):
    count += 1
    for j in range(0, 1000, 100):
        # TODO Перенесите это условие на уровень выше, во внешний цикл и меняйте
        #  начальное значение диапазона. Сейчас проверка выполняется для каждого кирпича.
        #  После переделки проверка будет проводиться для каждого ряда.
        if count % 2 == 1:
            j -= 50
        left_bottom = simple_draw.Point(j, i)
        right_top = simple_draw.Point(j + 100, i + 50)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=simple_draw.COLOR_DARK_RED, width=2)


simple_draw.pause()
