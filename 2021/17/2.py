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

hit_count = 0
for x_velo in range(-NUM_STEPS, NUM_STEPS):
    for y_velo in range(-NUM_STEPS, NUM_STEPS):
        hit_target = steps_for_velocity(x_velo, y_velo, X_MIN, X_MAX, Y_MIN, Y_MAX)

        if hit_target is not None:
            hit_count += 1

print(hit_count)