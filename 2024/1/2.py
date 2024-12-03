with open("input.txt") as f:
    left = []
    right = {}
    for line in f:
        split = line.strip().split("   ")
        left.append(int(split[0]))
        right_num = int(split[1])

        if right_num in right:
            right[right_num] += 1
        else:
            right[right_num] = 1

similarity_sum = 0

for num in left:
    try:
        similarity_sum += num * right[num]
    except KeyError:
        pass

print(similarity_sum)