from Pieces.Piece import Piece

class King(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self, board):
        moveList = []
        for move in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
            if ((7 >= self.rank + move[0] >= 0) and
                (7 >= self.file + move[1] >= 0) and
                (not issubclass(type(board[self.rank + move[0], self.file + move[1]]), Piece))):
                moveList.append((self.rank + move[0], self.file + move[1]))
            elif ((7 >= self.rank + move[0] >= 0) and
                  (7 >= self.file + move[1] >= 0) and
                  (board[self.rank+move[0], self.file+move[1]].color != self.color)):
                moveList.append((self.rank+move[0], self.file+move[1]))
        return moveList
    def moveTo(self, new_rank, new_file, board):
        board[self.rank, self.file] = None
        board[new_rank, new_file] = self
        self.rank = new_rank
        self.file = new_file

    def __str__(self):
        return self.color + "King"