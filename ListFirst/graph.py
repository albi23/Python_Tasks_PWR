import math


def draw_function(screen_width, screen_height):
    from numpy import linspace
    screen = [[" " for _ in range(screen_width)] for _ in range(screen_height)]
    # print(screen)
    # f = input("Enter a function: f(x) = ")
    # start = float(input("Enter start of the range: "))
    # end = float(input("Enter end of the range: "))
    f = lambda x: math.cos(x)
    start = -math.pi
    end = math.pi
    if start >= end:
        return "start >= end !"
    range_length = end - start

    f_args = linspace(0, screen_width, num=screen_width)
    f_vals = [f(x) for x in linspace(start, end, num=screen_width)]
    y_sup = max(f_vals)
    y_inf = min(f_vals)
    y_length = y_sup - y_inf

    for i, val in enumerate(f_vals):
        row = screen[math.floor((screen_height - 1) / y_length * (val - y_inf))]
        row[i] = "*"


    y_axis = math.floor((screen_height - 1) / y_length * (0 - y_inf))
    if y_axis in range(screen_height):
        for i in range(len(screen[y_axis])):
            screen[y_axis][i] = "-"

    x_axis = math.floor((screen_width - 1) / range_length * (0 - start))
    if x_axis in range(screen_width):
        for row in screen:
            row[x_axis] = "|"
    for row in reversed(screen):
        line = "".join(row)
        print(line)

draw_function(80, 24)