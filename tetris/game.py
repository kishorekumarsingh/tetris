"""
game.py contains the gameplay logic
"""

import random
from .board import Board, BOARD_SIZE
from .piece import Piece
from .pieces import PIECES
from .state import RunningState, GameOverState


class Game:
    def __init__(self):
        self.state = RunningState()
        self.board = Board()
        self.piece = None
        self.piece_pos = None
        self.spawn_piece()

    def set_state(self, new_state):
        self.state = new_state

    def spawn_piece(self):
        """
        Spawns a new piece at the top center of the Tetris board.
        If the piece cannot be spawned normally, it is spawned randomly
        at any horizontal position on the top row.
        :return:
        """
        piece_str = random.choice(PIECES)
        self.piece = Piece(piece_str)

        # Try to spawn the piece at the center first
        center_pos = (0, (BOARD_SIZE[1] - len(self.piece.piece)) // 2)
        if self.board.is_valid_move(self.piece.piece, center_pos):
            self.piece_pos = center_pos
            return

        # If the center position is not valid, spawn at a random horizontal position
        random_pos = (0, random.randint(0, BOARD_SIZE[1] - len(self.piece.piece[0])))
        if self.board.is_valid_move(self.piece.piece, random_pos):
            self.piece_pos = random_pos
            return

        # If no valid positions are found, set the piece position to None
        self.piece_pos = None

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
        return self.piece_pos is None

    def play(self):
        """
        Handles user interaction and gameplay logic
        :return:
        """
        while not isinstance(self.state, GameOverState):
            self.draw_board()

            user_input = input("Enter a move (a, d, w, s, space, q): ").lower()
            if user_input == 'q':
                break

            self.state.handle_input(self, user_input)
            self.state.update(self)

            # Check if the game is over
            if self.game_over():
                print("Game over!")
                self.set_state(GameOverState())
