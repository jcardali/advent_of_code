x = 0
y = 0

FORWARD = "forward"
DOWN = "down"
UP = "up"

with open("input.txt") as f:
    for line in f:
        [direction, str_units] = line.split(" ")
        units = int(str_units)
        if direction == FORWARD:
            x += units
        elif direction == DOWN:
            y += units
        elif direction == UP:
            y -= units
        print(x, y)

print(x * y)