# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    """Вода"""

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()
        elif isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Вода'


class Air:
    """Воздух"""

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Воздух'


class Fire:
    """Огонь"""

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Огонь'


class Earth:
    """Земля"""

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Mud()
        elif isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Земля'


class Storm:
    """Шторм"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Шторм'


class Steam:
    """Пар"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Пар'


class Mud:
    """Грязь"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Грязь'


class Lightning:
    """Молния"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Молния'


class Dust:
    """Пыль"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Пыль'


class Lava:
    """Лава"""

    def __add__(self, other):
        if isinstance(other, Emptiness):
            return Emptiness()
        else:
            return None

    def __str__(self):
        return 'Лава'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Earth(), '=', Fire() + Earth())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.

class Emptiness:
    """Пустота"""

    def __add__(self, other):
        """При добавлении чего угодно к пустоте, всегда получается пустота"""
        return Emptiness()

    def __str__(self):
        return 'Пустота'


print(Emptiness(), '+', Air(), '=', Emptiness() + Air())
print(Emptiness(), '+', Earth(), '=', Emptiness() + Earth())
