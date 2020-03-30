import simple_draw as sd


def draw_sun(_x, _y, _color=sd.COLOR_YELLOW, _step=30):
    # """Функция рисуюет смайл"""
    for i in range(0, 360, _step):
        sd.vector(start=sd.get_point(_x, _y), angle=i, length=80, color=_color)
    center_position = sd.Point(_x, _y)
    radius = 50
    sd.circle(center_position=center_position, radius=radius, color=sd.COLOR_YELLOW, width=0)
