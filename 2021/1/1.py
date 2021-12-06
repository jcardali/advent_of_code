prev_num = 0
increases = 0

with open("input.txt") as f:
    for line in f:
        cur_num = int(line)
        if cur_num > prev_num:
            increases += 1
        prev_num = cur_num

print(increases-1)
