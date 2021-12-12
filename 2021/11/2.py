from shared import parse_input, increment_energy_for_step, do_flashes, reset_flashes

NUM_STEPS = 1000
octopuses = parse_input()


for step in range(0, NUM_STEPS):
    flash_indices = []
    flash_set = set()

    increment_energy_for_step(octopuses, flash_indices, flash_set)
    do_flashes(octopuses, flash_indices, flash_set)
    reset_flashes(octopuses)

    if len(flash_set) == 100:
        print(step + 1)
        break

