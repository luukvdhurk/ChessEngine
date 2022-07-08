import Piece

class Bishop(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self):
        pass

    def moveTo(self, rank, file):
        pass

    def __str__(self):
        return self.color + "Bishop"