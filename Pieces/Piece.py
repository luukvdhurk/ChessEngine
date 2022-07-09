
class Piece():
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self, board):
        pass

    def moveTo(self, rank, file):
        pass

    def __str__(self):
        return "This is a generic string value."