from shared import parse_input, is_lower

height_map = parse_input()


def find_basin_helper(row_idx, col_idx, height, current_basin):
    try:
        if row_idx >= 0 and col_idx >= 0 and height_map[row_idx][col_idx] > height and height_map[row_idx][col_idx] != 9:
            current_basin.add((row_idx, col_idx))
            current_basin = find_basin(row_idx, col_idx, height_map[row_idx][col_idx], current_basin)
    except IndexError:
        pass
    return current_basin


def find_basin(row_idx, col_idx, height, current_basin):
    current_basin = find_basin_helper(row_idx - 1, col_idx, height, current_basin)
    current_basin = find_basin_helper(row_idx + 1, col_idx, height, current_basin)
    current_basin = find_basin_helper(row_idx, col_idx - 1, height, current_basin)
    current_basin = find_basin_helper(row_idx, col_idx + 1, height, current_basin)
    return current_basin


basins = []
for row_idx, row in enumerate(height_map):
    for height_idx, height in enumerate(row):
        if is_lower(row_idx - 1, height_idx, height, height_map) and is_lower(row_idx + 1, height_idx, height, height_map) \
                and is_lower(row_idx, height_idx - 1, height, height_map) and is_lower(row_idx, height_idx + 1, height, height_map):
            basins.append(find_basin(row_idx, height_idx, height, {(row_idx, height_idx)}))

biggest_three_basins = sorted(basins, key=len, reverse=True)[:3]
print(len(biggest_three_basins[0]) * len(biggest_three_basins[1]) * len(biggest_three_basins[2]))
