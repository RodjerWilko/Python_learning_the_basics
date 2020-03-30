# TODO Используйте полный путь к модулям, относительно основного
#  модуля программы. Добавьте перед draw перед модулями из пакета draw.
# TODO Постарайтесь не смешивать импорты своих модулей с импортами библиотек.
import simple_draw as sd

import smile
import triangle
import wall


def draw_house():
    wall.draw_wall()
    sd.rectangle(left_bottom=sd.get_point(400, 0), right_top=sd.get_point(850, 400), color=sd.COLOR_YELLOW, width=1)
    sd.rectangle(left_bottom=sd.get_point(550, 100), right_top=sd.get_point(700, 250), color=sd.COLOR_DARK_BLUE)
    smile.draw_smile(_x=625, _y=175, color=sd.COLOR_YELLOW)
    triangle.draw_triangle(_start_point=sd.get_point(400, 400), _angle=0, _length=450, )


# sd.pause()
