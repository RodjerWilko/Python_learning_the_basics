import simple_draw as sd

import draw.smile
import draw.triangle
import draw.wall


def draw_house():
    draw.wall.draw_wall()
    sd.rectangle(left_bottom=sd.get_point(400, 0), right_top=sd.get_point(850, 400), color=sd.COLOR_YELLOW, width=1)
    sd.rectangle(left_bottom=sd.get_point(550, 100), right_top=sd.get_point(700, 250), color=sd.COLOR_DARK_BLUE)
    draw.smile.draw_smile(_x=625, _y=175, color=sd.COLOR_YELLOW)
    draw.triangle.draw_triangle(_start_point=sd.get_point(400, 400), _angle=0, _length=450, )

# sd.pause()
