name = input("Hello, what's your name?")

if not isinstance(name, str) or len(name) <= 2:
    print("Your name is too short")
else:
    board_size_input = input(f"{name}, please choose board size:")

    if board_size_input.isdigit():
        board_size = int(board_size_input)

        if 0 <= board_size <= 26:
            number_of_mines_input = input(f"{name} for board size {board_size}, choose number of mines to allocate:")

            if number_of_mines_input.isdigit():
                number_of_mines = int(number_of_mines_input)

                if not (0 < number_of_mines < board_size / 2):
                    print(f"{name}, you entered an illegal number of mines")
            else:
                print(f"{name}, you entered an illegal number of mines")
        else:
            print(f"{name}, you entered an illegal board size")
    else:
        print(f"{name}, you entered an illegal board size")
