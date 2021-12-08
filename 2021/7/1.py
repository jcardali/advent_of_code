from sys import maxsize


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
for i in range(min, max + 1):
    fuel = 0

    for crab in crabs:
        position = int(crab)
        fuel += abs(i - position)

    if fuel < min_fuel:
        min_fuel = fuel

print(min_fuel)
