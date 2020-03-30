import simple_draw as sd


def draw_tree(_start_point, _angle, _length, _delta=30, _color=sd.COLOR_YELLOW):
    if _length < 10:
        return
    v1 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v2 = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
    v1.draw(color=_color)
    next_point = v1.end_point
    next_point2 = v2.end_point
    next_angle = _angle - _delta
    next_angle2 = _angle + _delta
    next_length = _length * .75
    draw_tree(_start_point=next_point, _angle=next_angle, _length=next_length, _color=_color)
    draw_tree(_start_point=next_point2, _angle=next_angle2, _length=next_length, _color=_color)


# root_point = sd.get_point(300, 30)
# draw_tree(_start_point=root_point, _angle=90, _length=100)
