def parse_input():
    octopuses = []
    with open("input.txt") as f:
        for line in f:
            new_octopuses = []
            for energy in line.rstrip():
                new_octopuses.append(int(energy))
            octopuses.append(new_octopuses)
    return octopuses


def increment_energy_for_step(octopuses, flash_indices, flash_set):
    for y_idx, row in enumerate(octopuses):
        for x_idx, octopus in enumerate(row):
            octopuses[y_idx][x_idx] += 1
            if octopuses[y_idx][x_idx] > 9:
                flash_indices.append((y_idx, x_idx))
                flash_set.add((y_idx, x_idx))


def increment_energy(y_idx, x_idx, octopuses, flash_indices, flash_set):
    try:
        if y_idx >= 0 and x_idx >= 0:
            octopuses[y_idx][x_idx] += 1
            if octopuses[y_idx][x_idx] > 9 and (y_idx, x_idx) not in flash_set:
                flash_indices.append((y_idx, x_idx))
                flash_set.add((y_idx, x_idx))
    except IndexError:
        pass


def flash(y_idx, x_idx, octopuses, flash_indices, flash_set):
    increment_energy(y_idx - 1, x_idx, octopuses, flash_indices, flash_set)
    increment_energy(y_idx - 1, x_idx + 1, octopuses, flash_indices, flash_set)
    increment_energy(y_idx, x_idx + 1, octopuses, flash_indices, flash_set)
    increment_energy(y_idx + 1, x_idx + 1, octopuses, flash_indices, flash_set)
    increment_energy(y_idx + 1, x_idx, octopuses, flash_indices, flash_set)
    increment_energy(y_idx + 1, x_idx - 1, octopuses, flash_indices, flash_set)
    increment_energy(y_idx, x_idx - 1, octopuses, flash_indices, flash_set)
    increment_energy(y_idx - 1, x_idx - 1, octopuses, flash_indices, flash_set)


def do_flashes(octopuses, flash_indices, flash_set):
    while len(flash_indices) > 0:
        flash_tuple = flash_indices.pop()
        flash(flash_tuple[0], flash_tuple[1], octopuses, flash_indices, flash_set)


def reset_flashes(octopuses):
    for y_idx, row in enumerate(octopuses):
        for x_idx, octopus in enumerate(row):
            if octopuses[y_idx][x_idx] > 9:
                octopuses[y_idx][x_idx] = 0
