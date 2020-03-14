import unittest
import globVar
import board
import pieces
from square import Square
import utils


grid = []


class TestBoard(unittest.TestCase):
    def test_populate(self):
        # Generate empty chess board
        global grid
        b = board
        pawnCount = 0
        rookCount = 0
        knightCount = 0
        bishopCount = 0
        queenCount = 0
        kingCount = 0

        b.grid = []
        for i in range(16):
            b.grid.append([])
            for j in range(16):
                b.grid[i].append(Square(False, "b", pieces.Piece("none", "none"), i, j))
            # Fill board with pieces

            # black
            plr = "b"
            b.Grid(0, 0).piece = pieces.Rook(plr, "rook")
            b.Grid(0, 1).piece = pieces.Knight(plr, "knight")
            b.Grid(0, 2).piece = pieces.Bishop(plr, "bishop")
            b.Grid(0, 3).piece = pieces.Queen(plr, "queen")
            b.Grid(0, 4).piece = pieces.King(plr, "king")
            b.Grid(0, 5).piece = pieces.Bishop(plr, "bishop")
            b.Grid(0, 6).piece = pieces.Knight(plr, "knight")
            b.Grid(0, 7).piece = pieces.Rook(plr, "rook")

        for i in range(8):
            for j in range(8):
                if b.Grid(i, j).piece.type == "pawn":
                    pawnCount = pawnCount + 1
                if b.Grid(i, j).piece.type == "rook":
                    rookCount = rookCount + 1
                if b.Grid(i, j).piece.type == "knight":
                    knightCount = knightCount + 1
                if b.Grid(i, j).piece.type == "bishop":
                    bishopCount = bishopCount + 1
                if b.Grid(i, j).piece.type == "queen":
                    queenCount = queenCount + 1
                if b.Grid(i, j).piece.type == "king":
                    kingCount = kingCount + 1

        self.assertTrue(rookCount == 2)
        self.assertTrue(knightCount == 2)
        self.assertTrue(bishopCount == 2)
        self.assertTrue(queenCount == 1)
        self.assertTrue(kingCount == 1)


unittest.main()
