# Example
x_min = 20
x_max = 30
y_min = -10
y_max = -5

# Real
# x_min = 169
# x_max = 206
# y_min = -108
# y_max = -68

max_height = 0
max_height_x = 0
max_height_y = 0
NUM_STEPS = 30


def steps_for_velocity(x_velo, y_velo):
    x = 0
    y = 0
    max_y = 0

    hit_target = False
    missed_target = False

    while hit_target is False and missed_target is False:
        x, y, x_velo, y_velo = step(x, y, x_velo, y_velo)
        # print(x, y, x_velo, y_velo)

        if y > max_y:
            max_y = y

        if x_min <= x <= x_max and y_min <= y <= y_max:
            hit_target = True

        if x > x_max or y < y_min:
            missed_target = True

    return max_y if hit_target else 0
    # max_height = max_y
    # max_height_x = x_velocity_initial
    # max_height_y = y_velocity_initial


def step(x, y, x_velo, y_velo):
    x += x_velo
    y += y_velo
    y_velo -= 1

    if x_velo > 0:
        x_velo -= 1
    elif x_velo < 0:
        x_velo += 1

    return x, y, x_velo, y_velo


for x_velo in range(-NUM_STEPS, NUM_STEPS):
    for y_velo in range(-NUM_STEPS, NUM_STEPS):
        max_y = steps_for_velocity(x_velo, y_velo)

        if max_y > max_height:
            max_height = max_y
            max_height_x = x_velo
            max_height_y = y_velo

print(max_height, (max_height_x, max_height_y))
# print(steps_for_velocity(7, 2))
# print(steps_for_velocity(6, 3))
# print(steps_for_velocity(9, 0))
# print(steps_for_velocity(-17, 4))
# print(steps_for_velocity(6, 9))