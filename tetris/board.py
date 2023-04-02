"""
board.py contains the logic related to board
"""

# Immutable board_size tuple
BOARD_SIZE = (12, 12)


class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(BOARD_SIZE[1])] for _ in range(BOARD_SIZE[0])]

    # TODO : implement function
    def is_valid_move(self, piece, pos):
        """
        A valid move is defined thus: if the piece, drawn at its new location,
        is not outside the bounds of the board, and does not overlap any pieces
        that previously fell, then the move is valid.
        :param piece:
        :param pos:
        :return:
        """

    # TODO : implement function
    def update_board(self, piece, pos):
        """
        Update the board based on the piece and the new position
        :param piece:
        :param pos:
        :return:
        """
