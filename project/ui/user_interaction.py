name = None
board_size = None
number_of_mines = None

name_input = input("Hello, what's your name?")

# Check for name conditions
if isinstance(name_input, str) and len(name_input) > 2:
    name = name_input
else:
    print("Your name is too short")

if name:
    board_size_input = input(f"{name}, please choose board size:")

    if board_size_input.isdigit():
        temp_board_size = int(board_size_input)

        # Check for board_size conditions
        if 0 <= temp_board_size <= 26:
            board_size = temp_board_size

            number_of_mines_input = input(f"{name} for board size {board_size}, choose number of mines to allocate:")

            if number_of_mines_input.isdigit():
                temp_number_of_mines = int(number_of_mines_input)

                # Check for number_of_mines conditions
                if 0 < temp_number_of_mines < board_size / 2:
                    number_of_mines = temp_number_of_mines
                else:
                    print(f"{name} you entered an illegal number of mines")
            else:
                print(f"{name} you entered an illegal number of mines")
        else:
            print(f"{name} you entered an illegal board size")
    else:
        print(f"{name} you entered an illegal board size")

print(f"Name: {name}, Board Size: {board_size}, Number of Mines: {number_of_mines}")
