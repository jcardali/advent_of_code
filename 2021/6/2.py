NUM_DAYS = 256

with open("input.txt") as f:
    school = {}
    for i in range(0, 9):
        school[i] = 0
    for fish in f.readline().split(","):
        school[int(fish)] += 1

current_day = 0
while current_day < NUM_DAYS:
    for timer, count in sorted(school.items(), reverse=True):
        if timer == 0:
            school[6] += count
            school[8] = count
        else:
            school[timer - 1] = count

    current_day += 1

num_fish = 0
for count in school.values():
    num_fish += count

print(num_fish)
