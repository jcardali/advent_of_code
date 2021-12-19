from shared import steps_for_velocity

# Example
# X_MIN = 20
# X_MAX = 30
# Y_MIN = -10
# Y_MAX = -5
# NUM_STEPS = 35

# Real
X_MIN = 169
X_MAX = 206
Y_MIN = -108
Y_MAX = -68
NUM_STEPS = 300

max_height = 0
for x_velo in range(0, NUM_STEPS):
    for y_velo in range(0, NUM_STEPS):
        max_y = steps_for_velocity(x_velo, y_velo, X_MIN, X_MAX, Y_MIN, Y_MAX)

        if max_y and max_y > max_height:
            max_height = max_y

print(max_height)
