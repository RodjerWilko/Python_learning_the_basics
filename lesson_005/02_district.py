# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

import district.central_street.house1.room1
import district.central_street.house1.room2
import district.central_street.house2.room1
import district.central_street.house2.room2
import district.soviet_street.house1.room1
import district.soviet_street.house1.room2
import district.soviet_street.house2.room1
import district.soviet_street.house2.room2

all_mans = []


def add_to_list(_list):
    for man in _list:
        all_mans.append(man)


add_to_list(district.central_street.house1.room1.folks)
add_to_list(district.central_street.house1.room2.folks)
add_to_list(district.central_street.house2.room1.folks)
add_to_list(district.central_street.house2.room2.folks)
add_to_list(district.soviet_street.house1.room1.folks)
add_to_list(district.soviet_street.house1.room2.folks)
add_to_list(district.soviet_street.house2.room1.folks)
add_to_list(district.soviet_street.house2.room2.folks)

print('На районе живут ', ', '.join(all_mans))





