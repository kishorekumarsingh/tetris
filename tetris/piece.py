"""
piece.py contains the logic related to the pieces
"""


class Piece:
    def __init__(self, piece_str):
        self.piece = [list(row) for row in piece_str.split('\n')]

    def rotate(self, rotation):
        # Input move is <a> or <d> : do not rotate
        if rotation == 0:
            return self.piece

        # Input move is <s> : rotate clockwise
        if rotation > 0:
            # TODO
            return self.piece

        # Input move is <w>
        # TODO
        return self.piece
