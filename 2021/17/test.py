from shared import steps_for_velocity

X_MIN = 20
X_MAX = 30
Y_MIN = -10
Y_MAX = -5

assert steps_for_velocity(7, 2, X_MIN, X_MAX, Y_MIN, Y_MAX) == 3
assert steps_for_velocity(6, 3, X_MIN, X_MAX, Y_MIN, Y_MAX) == 6
assert steps_for_velocity(9, 0, X_MIN, X_MAX, Y_MIN, Y_MAX) == 0
assert steps_for_velocity(17, -4, X_MIN, X_MAX, Y_MIN, Y_MAX) is None
assert steps_for_velocity(6, 9, X_MIN, X_MAX, Y_MIN, Y_MAX) == 45
