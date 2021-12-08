from sys import maxsize


def get_fuel_cost(steps):
    fuel = 0
    for i in range(1, steps + 1):
        fuel += i
    return fuel


with open("input.txt") as f:
    crabs = f.readline().split(",")

min = 0
max = 0

for crab in crabs:
    position = int(crab)
    if position < min:
        min = position

    if position > max:
        max = position

min_fuel = maxsize
min_position = 0
for i in range(min, max + 1):
    fuel = 0

    for crab in crabs:
        position = int(crab)
        fuel += get_fuel_cost(abs(i - position))

    if fuel < min_fuel:
        min_fuel = fuel
        min_position = i

print(min_position, min_fuel)
