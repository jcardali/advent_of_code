with open("input.txt") as f:
    reports = []
    for line in f:
        reports.append(line.strip().split(" "))

count = 0

for idx, report in enumerate(reports):
    prev = None
    is_increasing = None
    is_safe = True

    for level in report:
        level = int(level)
        if prev is None:
            prev = level
            continue
        diff = level - prev
        prev = level
        if is_increasing is None:
            is_increasing = diff > 0
        if (is_increasing and diff <= 0) or (not is_increasing and diff >= 0):
            is_safe = False
        abs_diff = abs(diff)
        if abs_diff < 1 or abs_diff > 3:
            is_safe = False

    if is_safe:
        count += 1

print(count)

