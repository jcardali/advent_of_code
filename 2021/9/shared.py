def parse_input():
    height_map = []
    with open("input.txt") as f:
        for row_idx, line in enumerate(f):
            height_map.append([])
            for height in line.rstrip():
                height_map[row_idx].append(int(height))
    return height_map


def is_lower(row_idx, col_idx, current_height, height_map):
    try:
        if row_idx >= 0 and col_idx >= 0:
            if height_map[row_idx][col_idx] > current_height:
                return True
            else:
                return False
        else:
            return True
    except IndexError:
        return True
