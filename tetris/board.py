"""
board.py contains the logic related to board
"""

# Immutable board_size tuple
BOARD_SIZE = (12, 12)


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE[1])] for _ in range(BOARD_SIZE[0])]

    def is_valid_move(self, piece, pos):
        """
        A valid move is defined thus: if the piece, drawn at its new location,
        is not outside the bounds of the board, and does not overlap any pieces
        that previously fell, then the move is valid.
        :param piece:
        :param pos:
        :return:
        """
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell == ' ':
                    continue
                x, y = pos[0] + i, pos[1] + j
                if y < 0 or y >= BOARD_SIZE[1] or (x >= BOARD_SIZE[0]):
                    return False
                if x >= 0 and self.board[x][y] != ' ':
                    return False
        return True

    def update_board(self, piece, piece_pos):
        """
        Update the board based on the piece and the new position
        :param piece:
        :param piece_pos:
        :return:
        """
        for i, row in enumerate(piece):
            for j, cell in enumerate(row):
                if cell != ' ':
                    self.board[piece_pos[0] + i][piece_pos[1] + j] = cell
