def is_name_valid(name):
    return isinstance(name, str) and len(name) > 2


def is_board_size_valid(board_size):
    return 1 <= board_size <= 26


def is_number_of_mines_valid(board_size, number_of_mines):
    return 0 < number_of_mines < board_size / 2


def register_user():
    player_name = None
    board_size = None
    mines_num = None

    name_input = input("Hello, what's your name?")

    if not is_name_valid(name_input):
        print("Your name is too short")
        return None, None, None

    player_name = name_input
    board_size_input = input(f"{player_name}, please choose board size:")

    if not board_size_input.isdigit() or not is_board_size_valid(int(board_size_input)):
        print(f"{player_name}, you entered illegal board size")
        return None, None, None

    board_size = int(board_size_input)
    mines_num_input = input(f"{player_name} for board size {board_size}, choose number of mines to allocate:")

    if not mines_num_input.isdigit() or not is_number_of_mines_valid(board_size, int(mines_num_input)):
        print(f"{player_name}, you entered illegal number of mines")
        return None, None, None

    mines_num = int(mines_num_input)
    return player_name, board_size, mines_num


player_name, board_size, mines_num = register_user()
print(player_name, board_size, mines_num)