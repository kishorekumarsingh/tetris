"""
game.py contains the gameplay logic
"""

import random
from board import Board, BOARD_SIZE
from piece import Piece
from pieces import PIECES


class Game:
    def __init__(self):
        self.board = Board()
        self.piece = None
        self.piece_pos = None
        self.spawn_piece()

    def spawn_piece(self):
        """
        Spawns a new piece at the top center of the tetris board
        :return:
        """
        piece_str = random.choice(PIECES)
        self.piece = Piece(piece_str)
        self.piece_pos = (0, (BOARD_SIZE[1] - len(self.piece.piece)) // 2)

    def draw_board(self):
        """
        Prints the current status of the board to stdout
        :return:
        """

    def move_piece(self, dx, rotation):
        """
        Moves the piece to a new position based on user input
        :param dx:
        :param rotation:
        :return:
        """

    def update_board(self):
        """
        Updates the board and spawns a new piece
        :return:
        """
        self.board.update_board(self.piece.piece, self.piece_pos)
        self.spawn_piece()

    def game_over(self):
        """
        Checks if the piece is within the bounds of the board
        :return:
        """
        return not self.board.is_valid_move(self.piece.piece, self.piece_pos)

    def play(self):
        """
        Handles user interaction and gameplay logic
        :return:
        """
        # Draw board
        # While game is not over
        #   Ask for user input
        #   check if input is valid
        #   Update board
        #   Draw board
