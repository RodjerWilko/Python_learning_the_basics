import simple_draw as sd


def draw_wall():
    k = 0
    for i in range(0, 400, 50):
        k = 50 - k
        for j in range(k + 400, 800, 100):
            left_bottom = sd.Point(j, i)
            right_top = sd.Point(j + 100, i + 50)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=sd.COLOR_DARK_RED, width=2)
