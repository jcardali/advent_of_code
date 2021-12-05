from shared import parse_input, play_number, is_winning_board, score_board


def play_badly(numbers, number_boards, marker_boards):
    winning_boards = set()
    for number in numbers:
        for idx, number_board in enumerate(number_boards):
            play_number(number_board, marker_boards[idx], number)
            if is_winning_board(marker_boards[idx]):
                if len(winning_boards) == len(number_boards) - 1 and idx not in winning_boards:
                    return score_board(number_board, marker_boards[idx]) * int(number)
                winning_boards.add(idx)


if __name__ == '__main__':
    numbers, number_boards, marker_boards = parse_input()
    print(play_badly(numbers, number_boards, marker_boards))
