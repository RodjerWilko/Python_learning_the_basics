import simple_draw as sd

snowflakes = []


def create_snowflake(n):
    global snowflakes
    for i in range(n):
        _x = sd.random_number(0, 800)
        _y = sd.random_number(700, 800)
        _length = sd.random_number(10, 35)
        _my_dict = {'x': _x, 'y': _y, 'length': _length}
        snowflakes.append(_my_dict)


def draw_snowflakes_color(color):
    sd.start_drawing()
    for i, snowflake in enumerate(snowflakes):
        sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
                     color=color)
    sd.finish_drawing()


def move_snowflakes():
    for snowflake in snowflakes:
        snowflake['y'] -= 15


def numbers_down():
    list_down_snowflake = []
    for i, snowflake in enumerate(snowflakes):
        if snowflake['y'] < 0:
            list_down_snowflake.append(i)
    return list_down_snowflake


def del_snowflakes(my_list):
    # TODO Вы удаляете не те снежинки.
    #  Если my_list содержит номера 2, 5, 6
    #  то из списка снежинок будут удалены снежинки
    #  с индексами 0, 1, 2.
    #  Для исправления возникающих ошибок при удалении снежинок
    #  нужно отсортировать my_list по убыванию. Тогда удаление снежинок
    #  в конце списка не будет оказывать влияние на снежинки в начале.
    for i in range(0, len(my_list)):
        del snowflakes[i]
