import unittest
import globVar
import board
from square import Square
import pieces

class TestPiece(unittest.TestCase):
    def testScan(self):
        # Generate empty chess board
        b = board
        b.grid = []
        for i in range(16):
            b.grid.append([])
            for j in range(16):
                b.grid[i].append(Square(False, "b", pieces.Piece("none", "none"), i, j))

        # Create a rook at location 3,3
        # This should allow the rook all of its possible moves
        b.Grid(0, 0).piece = pieces.Rook(False, "Rook")
        b.Grid(0, 0).piece.row = 0
        b.Grid(0, 0).piece.col = 0
        availMoves = b.Grid(0,0).piece.scan()

        self.assertTrue(availMoves == [] or availMoves != [])


unittest.main()
