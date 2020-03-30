import simple_draw as sd


def draw_figure(_sides, _start_point, _angle, _length, _angle_k):
    _end_point = _start_point
    for _ in range(_sides):
        v = sd.get_vector(start_point=_start_point, angle=_angle, length=_length)
        v.draw()
        _angle = _angle + _angle_k
        _start_point = v.end_point
    sd.line(start_point=_start_point, end_point=_end_point)


def draw_triangle(_start_point, _angle, _length):
    draw_figure(_sides=3, _start_point=_start_point, _angle=_angle, _length=_length, _angle_k=120)