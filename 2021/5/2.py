from shared import parse_line, record_coordinates, count_overlap_points, record_coordinate

coord_map = {}


def record_diagonal_coordinates(coord_map, x1, x2, y1, y2):
    x_diff = x1 - x2
    y_diff = y1 - y2
    x_increment = -1 if x_diff > 0 else 1
    y_increment = -1 if y_diff > 0 else 1

    for i in range(0, abs(x1 - x2) + 1):
        coord = f"{x1 + i * x_increment},{y1 + i * y_increment}"
        record_coordinate(coord_map, coord)


with open("input.txt") as f:
    for line in f:
        x1, y1, x2, y2 = parse_line(line)

        if x1 != x2 and y1 != y2 and abs(x1 - x2) != abs(y1 - y2):
            continue

        if x1 == x2 or y1 == y2:
            record_coordinates(coord_map, x1, x2, y1, y2)
        else:
            record_diagonal_coordinates(coord_map, x1, x2, y1, y2)

print(count_overlap_points(coord_map))
