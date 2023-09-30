def is_on_board(x: int, y: int, board: list[list]) -> bool:
    if 0 <= x < len(board) and 0 <= y < len(board[0]):
        return True
    return False


def safe_set_value(x: int, y: int, value: any, board: list[list]) -> bool:
    if is_on_board(x, y, board):
        board[x][y] = value
        return True
    return False
