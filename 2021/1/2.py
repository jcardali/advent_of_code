num_arr = []
sums = {}

with open("input.txt") as f:
    for line in f:
        cur_num = int(line)
        num_arr.append(cur_num)

    for idx, num in enumerate(num_arr):
        try:
            sums[idx] = num_arr[idx] + num_arr[idx+1] + num_arr[idx+2]
        except:
            pass

prev_sum = 0
increases = 0

for sum in sums.values():
    if sum > prev_sum:
        increases += 1
    prev_sum = sum

print(increases-1)
