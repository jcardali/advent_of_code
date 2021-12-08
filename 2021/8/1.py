ONE_LEN = len('cf')
FOUR_LEN = len('bcdf')
SEVEN_LEN = len('acf')
EIGHT_LEN = len('abcdefg')

count = 0
with open("input.txt") as f:
    for line in f:
        signals_and_outputs = line.rstrip().split(" | ")
        outputs = signals_and_outputs[1].split()

        for output in outputs:
            if len(output) in [ONE_LEN, FOUR_LEN, SEVEN_LEN, EIGHT_LEN]:
                count += 1

print(count)

