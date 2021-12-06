from shared import parse_line, record_coordinates, count_overlap_points

coord_map = {}

with open("input.txt") as f:
    for line in f:
        x1, y1, x2, y2 = parse_line(line)

        if x1 != x2 and y1 != y2:
            continue

        record_coordinates(coord_map, x1, x2, y1, y2)

print(count_overlap_points(coord_map))
