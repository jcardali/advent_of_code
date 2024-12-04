import re
from shared import do_mul, MUL_PATTERN

instructions = ""
with open("input.txt") as f:
    for line in f:
        instructions += line

matches = re.findall(MUL_PATTERN, instructions)

sum = 0
for match in matches:
    sum += do_mul(match)

print(sum)