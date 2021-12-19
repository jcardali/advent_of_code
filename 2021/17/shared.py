def step(x, y, x_velo, y_velo):
    x += x_velo
    y += y_velo
    y_velo -= 1

    if x_velo > 0:
        x_velo -= 1
    elif x_velo < 0:
        x_velo += 1

    return x, y, x_velo, y_velo


def steps_for_velocity(x_velo, y_velo, x_min, x_max, y_min, y_max):
    x = 0
    y = 0
    max_y = 0

    hit_target = False
    missed_target = False

    while hit_target is False and missed_target is False:
        x, y, x_velo, y_velo = step(x, y, x_velo, y_velo)

        if y > max_y:
            max_y = y

        if x_min <= x <= x_max and y_min <= y <= y_max:
            hit_target = True

        if x > x_max or y < y_min:
            missed_target = True

    return max_y if hit_target else None
