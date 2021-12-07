NUM_DAYS = 80

with open("input.txt") as f:
    school = f.readline().split(",")
    for idx, fish in enumerate(school):
        school[idx] = int(fish)

current_day = 0
while current_day < NUM_DAYS:
    new_fish = 0
    for idx, fish in enumerate(school):
        if fish == 0:
            school[idx] = 6
            new_fish += 1
        else:
            school[idx] -= 1
    for i in range(0, new_fish):
        school.append(8)
    current_day += 1

print(len(school))
