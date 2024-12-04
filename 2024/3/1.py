import re

instructions = ""
with open("input.txt") as f:
    for line in f:
        instructions += line

matches = re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

sum = 0
for match in matches:
    match = match.replace("mul(", "").replace(")", "")
    split = match.split(",")
    sum += int(split[0])*int(split[1])

print(sum)