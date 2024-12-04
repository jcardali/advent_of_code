import re

from shared import do_mul, MUL_DO_DONT_PATTERN

instructions = ""
with open("input.txt") as f:
    for line in f:
        instructions += line

matches = re.findall(MUL_DO_DONT_PATTERN, instructions)

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