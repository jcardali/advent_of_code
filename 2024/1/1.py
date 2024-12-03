with open("input.txt") as f:
    left = []
    right = []
    for line in f:
        split = line.strip().split("   ")
        left.append(int(split[0]))
        right.append(int(split[1]))

left.sort()
right.sort()

diff_sum = 0
for idx, num in enumerate(left):
    diff_sum += abs(num - right[idx])

print(diff_sum)