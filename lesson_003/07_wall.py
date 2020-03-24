# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

k = 0
for i in range(0, 1000, 50):
    # Есть хитрый трюк, позволяющий убрать условие. В цикле на каждой итерации меняем k:
    # k = 50 - k. В результате k поочерёдно будет меняться с 50 на 0 и наоборот.
    k = 50 - k
    for j in range(k, 1000, 100):
        left_bottom = simple_draw.Point(j, i)
        right_top = simple_draw.Point(j + 100, i + 50)
        simple_draw.rectangle(left_bottom=left_bottom, right_top=right_top, color=simple_draw.COLOR_DARK_RED, width=2)

simple_draw.pause()

# зачет!
