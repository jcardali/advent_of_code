counts_map = {}

with open("input.txt") as f:
    for line in f:
        for idx, char in enumerate(line.strip()):
            if idx not in counts_map:
                counts_map[idx] = {'0': 0, '1': 0}
            counts_map[idx][char] += 1

gamma_binary_str = ''
for idx in counts_map:
    if counts_map[idx]['0'] > counts_map[idx]['1']:
        gamma_binary_str += '0'
    else:
        gamma_binary_str += '1'

gamma_int = int(gamma_binary_str, 2)

epsilon_binary_str = ''
for char in gamma_binary_str:
    if char == '0':
        epsilon_binary_str += '1'
    else:
        epsilon_binary_str += '0'

epsilon_int = int(epsilon_binary_str, 2)

print(gamma_int * epsilon_int)
