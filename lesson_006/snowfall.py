import simple_draw as sd

snowflakes = []


def create_snowflake(n):
    # TODO Функция create_snowflake используется и для создания снежинок до начала цикла,
    #  и для добавления замены упавшим снежинкам. Это правильно.
    #  Но сейчая при вызове функции список snowflakes очищается.
    #  Из-за этого снегопад продолжается только для нескольких снежинок, чаще всего одной.
    global snowflakes
    snowflakes = []
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
    # TODO При удалении элемента списка, все элементы, стоявшие в списке после него,
    #  сдвигаются вперёд на одну позицию. Если в my_list больше одного элемента,
    #  то удаляютеся не те снежинки, которые нужно. Иногда может возникать ошибка
    #  при попытке удалить элемент на позиции, большей чем количество оставшихся элементов.
    for num in my_list:
        del snowflakes[num]
