from sys import maxsize

from shared import increment_map, compare_min_max

insertion_map = {}
pair_counts = {}
NUM_STEPS = 40


with open("input.txt") as f:
    template = f.readline().rstrip()
    f.readline()

    for line in f:
        pair, new_char = line.rstrip().split(" -> ")
        insertion_map[pair] = new_char

for i in range(0, len(template)):
    pair = template[i:i + 2]
    if len(pair) == 2:
        if pair not in pair_counts:
            pair_counts[pair] = 1
        else:
            pair_counts[pair] += 1

for i in range(0, NUM_STEPS):
    new_pairs_and_counts = []
    for pair, count in pair_counts.items():
        if pair in insertion_map:
            insertion_char = insertion_map[pair]
            left_pair = pair[0] + insertion_char
            right_pair = insertion_char + pair[1]
            pair_counts[pair] = 0
            new_pairs_and_counts.append((left_pair, right_pair, count))
    for pair_and_count in new_pairs_and_counts:
        left_pair, right_pair, count = pair_and_count
        increment_map(pair_counts, left_pair, count)
        increment_map(pair_counts, right_pair, count)

char_counts = {}
for pair, count in pair_counts.items():
    increment_map(char_counts, pair[0], count)
    increment_map(char_counts, pair[1], count)

min_count = maxsize
max_count = 0
for char, count in char_counts.items():
    if count % 2 != 0:
        count += 1
    count //= 2
    min_count, max_count = compare_min_max(min_count, max_count, count)

print(max_count - min_count)
