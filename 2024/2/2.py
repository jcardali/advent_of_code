from shared import is_report_safe

with open("input.txt") as f:
    reports = []
    for line in f:
        reports.append(line.strip().split(" "))

count = 0

for report in reports:
    safe_count = 0
    for idx, level in enumerate(report):
        maybe_safer_report = report[:idx] + report[idx+1:]
        if is_report_safe(maybe_safer_report):
            safe_count += 1

    if safe_count != 0:
        count += 1

print(count)

