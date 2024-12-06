global grid
grid = []

with open("input.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        grid.append(row)

count = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        # shifts = [
        #     [(0, 0), (0, 1), (0, 2), (0, 3)],
        #     [(0, 0), (1, 0), (2, 0), (3, 0)],
        #     [(0, 0), (1, 1), (2, 2), (3, 3)],
        #     [(0, 0), (1, -1), (2, -2), (3, -3)],
        # ]
        # for shift in shifts:
        #     try:
        #         word = grid[y + shift[0][0]][x + shift[0][0]] + grid[y + shift[1][0]][x + shift[1][1]] + grid[y + shift[2][0]][x + shift[2][1]] + grid[y + shift[3][0]][x + shift[3][1]]
        #         if word == "XMAS" or word == "SAMX":
        #             count += 1
        #     except IndexError:
        #         pass
        try:
            word = grid[y][x] + grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3]
            if word == "XMAS" or word == "SAMX":
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
            if word == "XMAS" or word == "SAMX":
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3]
            if word == "XMAS" or word == "SAMX":
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3]
            # Need to make sure our index doesn't go negative
            if (word == "XMAS" or word == "SAMX") and x >= 3:
                count += 1
        except IndexError:
            pass

print(count)

# def search(y, x, search_term):
#     if y < 0 or x < 0:
#         return False
#
#     try:
#         val = grid[y][x]
#     except IndexError:
#         return False

#     if val == search_term:
#         return True
#     if val == search_term[0]:
#         return (
#                 search(y + 1, x, search_term[1:]) or search(y - 1, x, search_term[1:]) or
#                 search(y, x + 1, search_term[1:]) or search(y, x - 1, search_term[1:]) or
#                 search(y + 1, x + 1, search_term[1:]) or search(y - 1, x - 1, search_term[1:]) or
#                 search(y + 1, x - 1, search_term[1:]) or search(y - 1, x + 1, search_term[1:])
#         )
#