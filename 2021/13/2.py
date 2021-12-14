from shared import parse_input, fold

points, folds = parse_input()

fold(points, folds)

max_x = 0
max_y = 0
for point in points:
    if point[0] > max_x:
        max_x = point[0]
    if point[1] > max_y:
        max_y = point[1]

for y in range(0, max_y + 1):
    row = []
    for x in range(0, max_x + 1):
        if (x, y) in points:
            row.append("#")
        else:
            row.append(" ")
    print("".join(row))
