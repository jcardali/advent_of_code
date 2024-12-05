search_term = "XMAS"

global grid
grid = []

with open("input.txt") as f:
    for line in f:
        row = []
        for char in line.strip():
            row.append(char)
        print(row)
        grid.append(row)

# shifts = [
#     (0, 1),
#     (0, -1),
# ]

"""

"""
count = 0
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        try:
            word = grid[y][x] + grid[y][x + 1] + grid[y][x + 2] + grid[y][x + 3]
            if word == "XMAS" or word == "SAMX":
                # print("horizontal", (y, x), (y, x + 1), (y, x + 2), (y, x + 3))
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x] + grid[y + 2][x] + grid[y + 3][x]
            if word == "XMAS" or word == "SAMX":
                # print("vertical", (y, x), (y + 1, x), (y + 2, x), (y + 3, x))
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x + 1] + grid[y + 2][x + 2] + grid[y + 3][x + 3]
            if word == "XMAS" or word == "SAMX":
                # print("diagonal right", (y, x), (y + 1, x + 1), (y + 2, x + 2), (y + 3, x + 3))
                count += 1
        except IndexError:
            pass

        try:
            word = grid[y][x] + grid[y + 1][x - 1] + grid[y + 2][x - 2] + grid[y + 3][x - 3]
            if (word == "XMAS" or word == "SAMX") and x >= 3:
                # print("diagonal left", (y, x), (y + 1, x - 1), (y + 2, x - 2), (y + 3, x - 3))
                count += 1
        except IndexError:
            pass

print(count)

# row_count = len(grid) - 1
# col_count = len(grid[0]) - 1
# print(row_count, col_count)

# def search(y, x, search_term):
#     if y < 0 or x < 0:
#         return False
#
#     try:
#         val = grid[y][x]
#     except IndexError:
#         return False
#
#     # print(y, x, search_term)
#
#     if val == search_term:
#         # print("here")
#         return True
#     if val == search_term[0]:
#         return (
#                 search(y + 1, x, search_term[1:]) or search(y - 1, x, search_term[1:]) or
#                 search(y, x + 1, search_term[1:]) or search(y, x - 1, search_term[1:]) or
#                 search(y + 1, x + 1, search_term[1:]) or search(y - 1, x - 1, search_term[1:]) or
#                 search(y + 1, x - 1, search_term[1:]) or search(y - 1, x + 1, search_term[1:])
#         )
#