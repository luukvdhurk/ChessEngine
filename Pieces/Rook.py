from Pieces.Piece import Piece

class Rook(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self, board):
        moveList = []
        #For each direction:
        #Add all positions to the list until you either hit a piece, or hit a border.
        original_rank = self.rank
        original_file = self.file
        for direction in [-1, 1]:
            while (7 >= original_rank + direction >= 0 and
                   7 >= original_file + direction >= 0 and
                   not issubclass(type(board[original_rank+1, original_file]), Piece)):
                moveList.append((original_rank + 1, original_file))
                original_rank = original_rank + 1
                original_file = original_file +1
            if (board[original_rank+1, original_file].color != self.color):
                moveList.append((self.rank+1, self.file))

    def moveTo(self, rank, file):
        pass

    def __str__(self):
        return self.color + "Rook"
