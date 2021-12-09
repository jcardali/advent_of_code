from shared import parse_input, is_lower

height_map = parse_input()

total_risk_level = 0
for row_idx, row in enumerate(height_map):
    for height_idx, height in enumerate(row):
        if is_lower(row_idx - 1, height_idx, height, height_map) and is_lower(row_idx + 1, height_idx, height, height_map) \
                and is_lower(row_idx, height_idx - 1, height, height_map) and is_lower(row_idx, height_idx + 1, height, height_map):
            total_risk_level += height + 1

print(total_risk_level)
