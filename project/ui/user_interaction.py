name = None
board_size = None
number_of_mines = None
continue_process = True

name_input = input("Hello, what's your name?")

# Check for name conditions
if isinstance(name_input, str) and len(name_input) > 2:
    name = name_input
else:
    print("Your name is too short")
    continue_process = False

if continue_process and name:
    board_size_input = input(f"{name}, please choose board size:")

    if board_size_input.isdigit():
        temp_board_size = int(board_size_input)

        if 1 <= temp_board_size <= 26:
            board_size = temp_board_size

            number_of_mines_input = input(f"{name} for board size {board_size}, choose number of mines to allocate:")

            if number_of_mines_input.isdigit():
                temp_number_of_mines = int(number_of_mines_input)

                if 0 < temp_number_of_mines < board_size / 2:
                    number_of_mines = temp_number_of_mines
                else:
                    print(f"{name} you entered illegal number of mines")
            else:
                print(f"{name} you entered illegal number of mines")
        else:
            print(f"{name} you entered illegal board size")
    else:
        print(f"{name} you entered illegal board size")

