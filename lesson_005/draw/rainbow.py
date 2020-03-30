import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def draw_rainbow(_i=0):
    center_position = sd.Point(1500, 50)
    radius = 400
    if _i == 1:
        k = -1
    else:
        k = 1
    for color in rainbow_colors[k]:
        color = rainbow_colors[sd.random_number(0, 6)]
        radius += 20
        sd.circle(center_position=center_position, radius=radius, color=color, width=20)
