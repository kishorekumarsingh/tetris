"""
piece.py contains the logic related to the pieces
"""


class Piece:
    def __init__(self, piece_str):
        self.piece = [list(row) for row in piece_str.split('\n')]

    def rotate(self, rotation):
        if rotation == 0:
            return self.piece

        if rotation > 0:
            return [list(row)[::-1] for row in zip(*self.piece)]

        return [list(row) for row in zip(*self.piece[::-1])]
