ONE_LEN = 2
FOUR_LEN = 4
SEVEN_LEN = 3
EIGHT_LEN = 7

count = 0
with open("input.txt") as f:
    for line in f:
        signals_and_outputs = line.rstrip().split(" | ")
        outputs = signals_and_outputs[1].split()

        for output in outputs:
            if len(output) in [ONE_LEN, FOUR_LEN, SEVEN_LEN, EIGHT_LEN]:
                count += 1

print(count)

