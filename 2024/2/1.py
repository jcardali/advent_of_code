from shared import is_report_safe

with open("input.txt") as f:
    reports = []
    for line in f:
        reports.append(line.strip().split(" "))

count = 0

for report in reports:
    if is_report_safe(report):
        count += 1

print(count)

