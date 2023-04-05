import unittest
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tetris.board import Board, BOARD_SIZE
from tetris.piece import Piece
from tetris.game import Game


class TestTetris(unittest.TestCase):
    def test_board_initialization(self):
        # Test if the board is initialized with correct dimensions
        board = Board()
        self.assertEqual(len(board.board), BOARD_SIZE[0])
        self.assertEqual(len(board.board[0]), BOARD_SIZE[1])

    def test_piece_initialization(self):
        # Test if the piece is initialized with the correct structure
        piece_str = "**\n**"
        piece = Piece(piece_str)
        self.assertEqual(piece.piece, [['*', '*'], ['*', '*']])

    def test_valid_move(self):
        # Test if a valid move is allowed
        game = Game()
        game.piece = Piece(" *\n**")
        game.piece_pos = (0, 5)

        # Ensure the piece is spawned
        self.assertIsNotNone(game.piece_pos)

        self.assertTrue(game.move_piece(-1, 0, 0))

    def test_invalid_move(self):
        # Test if an invalid move is not allowed
        game = Game()
        game.piece = Piece(" *\n**")
        game.piece_pos = (0, 0)

        # Ensure the piece is spawned
        self.assertIsNotNone(game.piece_pos)

        self.assertFalse(game.move_piece(-1, 0, 0))

    def test_edge_case_move(self):
        # Test an edge case for piece rotation near the board's boundaries
        game = Game()
        game.piece = Piece(" *\n**")
        game.piece_pos = (0, BOARD_SIZE[1] - 2)

        # Ensure the piece is spawned
        self.assertIsNotNone(game.piece_pos)

        self.assertTrue(game.move_piece(0, 0, -1))

    def test_game_over(self):
        # Test if the game over condition is detected
        game = Game()
        game.board.board[0] = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

        # Fill up the top row to simulate a game over scenario
        for i in range(BOARD_SIZE[1]):
            game.board.board[0][i] = '*'

        game.spawn_piece()

        # Check if the piece is not spawned (i.e., piece_pos is None)
        self.assertIsNone(game.piece_pos)

        # Check if the game is over
        self.assertTrue(game.game_over())


if __name__ == '__main__':
    unittest.main()
