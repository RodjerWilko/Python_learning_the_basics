import simple_draw as sd


def draw_smile(_x, _y, color):
    """Функция рисуюет смайл"""
    center_position_left_eye = sd.Point(_x - 15, _y + 15)
    center_position_right_eye = sd.Point(_x + 15, _y + 15)
    center_position = sd.Point(_x, _y)
    first_dot_smile = sd.Point(_x - 25, _y - 10)
    second_dot_smile = sd.Point(_x - 5, _y - 20)
    third_dot_smile = sd.Point(_x + 5, _y - 20)
    four_dot_smile = sd.Point(_x + 25, _y - 10)
    point_list = [first_dot_smile, second_dot_smile, third_dot_smile, four_dot_smile]
    radius = 50
    radius_eye = 5

    sd.circle(center_position=center_position_left_eye, radius=radius_eye, color=color, width=3)
    sd.circle(center_position=center_position_right_eye, radius=radius_eye, color=color, width=3)
    sd.sleep(0.001)
    sd.circle(center_position=center_position_left_eye, radius=radius_eye, color=sd.background_color, width=3)
    sd.circle(center_position=center_position_right_eye, radius=radius_eye, color=sd.background_color, width=3)
    sd.sleep(0.1)
    sd.circle(center_position=center_position, radius=radius, color=color, width=4)
    sd.lines(point_list=point_list, color=color, width=3)
