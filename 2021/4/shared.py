def parse_input():
    with open("input.txt") as f:
        numbers = f.readline().split(",")
        f.readline()  # skip empty line
        number_boards = []
        marker_boards = []

        new_number_board = []
        for line in f:
            row_numbers = line.strip().split()

            if not row_numbers:
                number_boards.append(new_number_board)
                marker_boards.append([[False, False, False, False, False] for i in range(5)])
                new_number_board = []
                continue

            new_row = []

            for row_number in row_numbers:
                new_row.append(row_number)

            new_number_board.append(new_row)

    return numbers, number_boards, marker_boards


def play_number(number_board, marker_board, called_number):
    for row_idx, row in enumerate(number_board):
        for col_idx, number in enumerate(row):
            if number_board[row_idx][col_idx] == called_number:
                marker_board[row_idx][col_idx] = True


def is_winning_row(marker_row):
    all_numbers = True
    for marker in marker_row:
        if not marker:
            all_numbers = False
    return all_numbers


def is_winning_col(marker_board, col_idx):
    all_numbers = True
    for row_idx, row in enumerate(marker_board):
        if not marker_board[row_idx][col_idx]:
            all_numbers = False
    return all_numbers


def is_winning_board(marker_board):
    for col_idx in range(0, 5):
        if is_winning_col(marker_board, col_idx):
            return True
    for row in marker_board:
        if is_winning_row(row):
            return True
    return False


def score_board(number_board, marker_board):
    score = 0
    for row_idx, row in enumerate(number_board):
        for col_idx, col in enumerate(row):
            if not marker_board[row_idx][col_idx]:
                score += int(number_board[row_idx][col_idx])
    return score