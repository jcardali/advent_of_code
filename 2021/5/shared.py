def parse_line(line):
    pair1, pair2 = line.rstrip().split(" -> ")
    x1_str, y1_str = pair1.split(",")
    x2_str, y2_str = pair2.split(",")

    return int(x1_str), int(y1_str), int(x2_str), int(y2_str)


def record_coordinate(coord_map, coord):
    if coord not in coord_map:
        coord_map[coord] = 1
    else:
        coord_map[coord] += 1


def record_coordinates(coord_map, x1, x2, y1, y2):
    if x1 > x2:
        temp = x1
        x1 = x2
        x2 = temp

    if y1 > y2:
        temp = y1
        y1 = y2
        y2 = temp

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            coord = f"{x},{y}"
            record_coordinate(coord_map, coord)


def count_overlap_points(coord_map):
    overlap_points = 0

    for k, v in coord_map.items():
        if v > 1:
            overlap_points += 1

    return overlap_points
