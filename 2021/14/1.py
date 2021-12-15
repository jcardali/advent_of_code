from shared import increment_map, compare_min_max

insertion_map = {}
NUM_STEPS = 10

with open("input_small.txt") as f:
    template = f.readline().rstrip()
    f.readline()

    for line in f:
        pair, new_char = line.rstrip().split(" -> ")
        if pair[0] not in insertion_map:
            insertion_map[pair[0]] = {}
        if pair[1] not in insertion_map[pair[0]]:
            insertion_map[pair[0]][pair[1]] = new_char

for i in range(0, NUM_STEPS):
    new_template = list(template)
    inserts = 0
    for j in range(0, len(template)):
        try:
            if insertion_map[template[j]][template[j + 1]]:
                new_template.insert(j + 1 + inserts, insertion_map[template[j]][template[j + 1]])
                inserts += 1
        except IndexError:
            pass
    template = "".join(new_template)

char_counts = {}

for char in template:
    increment_map(char_counts, char, 1)

min_count = 9999
max_count = 0
for char, count in char_counts.items():
    min_count, max_count = compare_min_max(min_count, max_count, count)

print(max_count - min_count)

