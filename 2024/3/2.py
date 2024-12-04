import re

from shared import do_mul

instructions = ""
with open("input.txt") as f:
    for line in f:
        instructions += line

matches = re.findall(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', instructions)

sum = 0
is_enabled = True

for match in matches:
    if match[0] and is_enabled:
        sum += do_mul(match[0])
    elif match[1]:
        is_enabled = True
    elif match[2]:
        is_enabled = False

print(sum)