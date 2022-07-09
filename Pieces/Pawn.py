from Pieces.Piece import Piece

class Pawn(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self, board):
        moveList = []
        if (self.color == "White"):
            if (board[self.rank+1, self.file] == None):
                moveList.append((self.rank+1, self.file))
            if (issubclass(type(board[self.rank+1, self.file+1]), Piece)):
                if(board[self.rank+1, self.file+1].color == "Black"):
                    moveList.append((self.rank+1, self.file+1))
            if (issubclass(type(board[self.rank+1, self.file-1]), Piece)):
                if (board[self.rank + 1, self.file - 1].color == "Black"):
                    moveList.append((self.rank+1, self.file-1))
        else:
            if (board[self.rank-1, self.file] == None):
                moveList.append((self.rank-1, self.file))
            if (issubclass(type(board[self.rank-1, self.file+1]), Piece)):
                if (board[self.rank - 1, self.file + 1].color == "White"):
                    moveList.append((self.rank-1, self.file+1))
            if (issubclass(type(board[self.rank-1, self.file-1]), Piece)):
                if (board[self.rank - 1, self.file + 1].color == "White"):
                    moveList.append((self.rank-1, self.file-1))
        return moveList



    def moveTo(self, new_rank, new_file, board):
        board[self.rank, self.file] = None
        board[new_rank, new_file] = self
        self.rank = new_rank
        self.file = new_file

        pass

    def __str__(self):
        return self.color + "Pawn"