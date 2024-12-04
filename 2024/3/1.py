import re
from shared import do_mul

instructions = ""
with open("input.txt") as f:
    for line in f:
        instructions += line

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

sum = 0
for match in matches:
    sum += do_mul(match)

print(sum)