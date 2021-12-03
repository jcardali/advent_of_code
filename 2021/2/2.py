x = 0
y = 0
aim = 0

FORWARD = "forward"
DOWN = "down"
UP = "up"

with open("input.txt") as f:
    for line in f:
        [direction, str_units] = line.split(" ")
        units = int(str_units)
        if direction == FORWARD:
            x += units
            y += aim * units
        elif direction == DOWN:
            aim += units
        elif direction == UP:
            aim -= units
        print(x, y)

print(x * y)