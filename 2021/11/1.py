from shared import parse_input, increment_energy_for_step, do_flashes, reset_flashes

NUM_STEPS = 100
octopuses = parse_input()


total_flashes = 0
for step in range(0, NUM_STEPS):
    flash_indices = []
    flash_set = set()

    increment_energy_for_step(octopuses, flash_indices, flash_set)
    do_flashes(octopuses, flash_indices, flash_set)
    reset_flashes(octopuses)

    total_flashes += len(flash_set)

print(total_flashes)

