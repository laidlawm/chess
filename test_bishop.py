import unittest
import globVar
import board
from square import Square
import pieces

class TestBishop(unittest.TestCase):
    def test_scan(self):

        # Generate empty chess board
        b = board
        b.grid = []
        for i in range(16):
            b.grid.append([])
            for j in range(16):
                b.grid[i].append(Square(False, "b", pieces.Piece("none", "none"), i, j))

        # Create a bishop at location 3,3
        # This should allow the bishop all of its possible moves
        b.Grid(0, 0).piece = pieces.Bishop(False, "Bishop")
        b.Grid(0, 0).piece.row = 0
        b.Grid(0, 0).piece.col = 0

        # # Ask the game to fetch possible moves for this piece
        availMoves = b.Grid(0, 0).piece.scan()

        given_moves = []
        for move in availMoves:
            given_moves.append([move.row, move.col])

        for i in range(len(given_moves)):
            self.assertTrue(given_moves[i][0] == given_moves[i][1])

unittest.main()
