counts_map = {}
values = set()


def get_rating(values, char1, char2):
    for idx in range(0, 12):
        zero_count = 0
        one_count = 0

        for value in values:
            if value[idx] == '0':
                zero_count += 1
            else:
                one_count += 1

        if zero_count > one_count:
            char = char1
        else:
            char = char2

        values = values.intersection(counts_map[idx][char])

        if len(values) == 1:
            return list(values)[0]


with open("input.txt") as f:
    for line in f:
        clean_line = line.strip()
        values.add(clean_line)
        for idx, char in enumerate(clean_line):
            if idx not in counts_map:
                counts_map[idx] = {'0': set(), '1': set()}
            counts_map[idx][char].add(clean_line)

oxygen_binary_str = get_rating(values, '0', '1')
co2_binary_str = get_rating(values, '1', '0')

oxygen_int = int(oxygen_binary_str, 2)
co2_int = int(co2_binary_str, 2)

print(oxygen_int * co2_int)