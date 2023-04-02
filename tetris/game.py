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
        temp_board = [[' ' for _ in range(BOARD_SIZE[1])] for _ in range(BOARD_SIZE[0])]

        for i, row in enumerate(self.board.board):
            for j, cell in enumerate(row):
                temp_board[i][j] = cell

        for i, row in enumerate(self.piece.piece):
            for j, cell in enumerate(row):
                if cell != ' ':
                    x, y = self.piece_pos[0] + i, self.piece_pos[1] + j
                    if 0 <= x < BOARD_SIZE[0] and 0 <= y < BOARD_SIZE[1]:
                        temp_board[x][y] = cell

        for row in temp_board:
            print('*' + ''.join(row) + '*')
        print('*' * (BOARD_SIZE[1] + 2))

    def move_piece(self, dx, dy, rotation):
        """
        Moves the piece to a new position based on user input
        :param dx:
        :param dy:
        :param rotation:
        :return:
        """
        new_piece = self.piece.rotate(rotation)
        new_pos = (self.piece_pos[0] + dy, self.piece_pos[1] + dx)

        if not self.board.is_valid_move(new_piece, new_pos):
            return False

        self.piece.piece = new_piece
        self.piece_pos = new_pos
        return True

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
        self.draw_board()
        # While game is not over
        while not self.game_over():
            #   Ask for user input
            user_input = input("Enter a move (a, d, w, s, space): ").lower()
            dx, dy, rotation = 0, 0, 0

            if user_input == 'a':
                dx = -1
            elif user_input == 'd':
                dx = 1
            elif user_input == 'w':
                rotation = -1
            elif user_input == 's':
                rotation = 1
            elif user_input == ' ':
                pass
            else:
                print("Invalid input. Try again.")
                continue

            #   check if input is valid
            valid_rotation = self.move_piece(dx, dy, rotation)

            if not valid_rotation:
                print("Invalid move. Try again.")
            else:
                if not self.move_piece(0, 1, 0):
                    self.update_board()

            self.draw_board()
