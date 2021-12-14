def parse_input():
    points = set()
    folds = []
    with open("input.txt") as f:
        for line in f:
            clean_line = line.rstrip()
            if "fold" in clean_line:
                left, right = clean_line.split("=")
                folds.append((left[-1], int(right)))
            else:
                try:
                    x, y = line.rstrip().split(",")
                    points.add((int(x), int(y)))
                except ValueError:
                    pass
    return points, folds


def fold(points, folds):
    for fold in folds:
        axis, amount = fold
        points_to_delete = set()
        points_to_add = set()

        if axis == 'x':
            for point in points:
                if point[0] > amount:
                    points_to_delete.add(point)
                    new_point = (amount - (point[0] - amount), point[1])
                    points_to_add.add(new_point)
        elif axis == 'y':
            for point in points:
                if point[1] > amount:
                    points_to_delete.add(point)
                    new_point = (point[0], amount - (point[1] - amount))
                    points_to_add.add(new_point)

        for point in points_to_delete:
            points.remove(point)

        for point in points_to_add:
            points.add(point)
