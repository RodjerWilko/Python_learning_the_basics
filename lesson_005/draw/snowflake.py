import simple_draw as sd


def snowflakes(_x1, _y1, _x2, _y2):
    def new_snowflake():
        _x = sd.random_number(_x1, _y1)
        _y = sd.random_number(_x2, _y2)
        _length = sd.random_number(10, 20)
        _my_dict = {'x': _x, 'y': _y, 'length': _length}
        snowflakes[i] = _my_dict

    snowflakes = {}

    for i in range(50):
        new_snowflake()

    while True:
        sd.start_drawing()
        for i, snowflake in snowflakes.items():

            sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
                         color=sd.background_color)
            snowflake['y'] -= 10
            if snowflake['x'] >= 340:
                snowflake['x'] += sd.random_number(-51, -50)
            snowflake['x'] += sd.random_number(-50, 50)
            sd.snowflake(center=sd.get_point(snowflake['x'], snowflake['y']), length=snowflake['length'],
                         color=sd.COLOR_WHITE)
            if snowflake['y'] < snowflake['length']:
                new_snowflake()
                continue
            sd.sleep(0.005)

        sd.finish_drawing()
        if sd.user_want_exit():
            break
    sd.pause()
