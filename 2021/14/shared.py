def increment_map(map, key, count):
    if key not in map:
        map[key] = count
    else:
        map[key] += count


def compare_min_max(min_count, max_count, count):
    if count < min_count:
        min_count = count
    if count > max_count:
        max_count = count
    return min_count, max_count
