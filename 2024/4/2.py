search_term = "XMAS"

global grid
grid = []

with open("input.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        # print(row)
        grid.append(row)

count = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        try:
            """
            M S       S M    M M    S S   
             A         A      A      A
            M S       S M    S S    M M
            """
            word = grid[y][x] + grid[y][x + 2] + grid[y + 1][x + 1] + grid[y + 2][x] + grid[y + 2][x + 2]
            if word == "MSAMS" or word == "SMASM" or word == "MMASS" or word == "SSAMM":
                count += 1
        except IndexError:
            pass

print(count)