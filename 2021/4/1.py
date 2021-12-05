from shared import parse_input, play_number, is_winning_board, score_board


def play(numbers, number_boards, marker_boards):
    for number in numbers:
        for idx, number_board in enumerate(number_boards):
            play_number(number_board, marker_boards[idx], number)
            if is_winning_board(marker_boards[idx]):
                return score_board(number_board, marker_boards[idx]) * int(number)


if __name__ == '__main__':
    numbers, number_boards, marker_boards = parse_input()
    print(play(numbers, number_boards, marker_boards))
