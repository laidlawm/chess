from pieces import Piece

class Queen(Piece):
    def __init__(self, color, type):
        Piece.__init__(self, color, type)

    def __str__(self):
        if(self.color == "W"):
            return "Q"
        else:
            return "q"
