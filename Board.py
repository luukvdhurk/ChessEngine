import numpy as np
from Pieces.Pawn import Pawn
from Pieces.Rook import Rook
from Pieces.Knight import Knight
from Pieces.Bishop import Bishop
from Pieces.Queen import Queen
from Pieces.King import King

class Board():
    def __init__(self):
        self.board = np.empty((8,8), dtype=np.object)

        for rank in range(0,len(self.board)):
            for file in range(0,len(self.board[rank])):
                if rank >=4:
                    color="Black"
                else:
                    color="White"
                if (rank == 1 or rank== 6):
                    self.board[rank,file] = Pawn(color, rank, file)
                if (rank%7 == 0):
                    if (file%7 == 0):
                        self.board[rank, file] = Rook(color, rank, file)
                    elif (file%7 == 1 or file%7 == 6):
                        self.board[rank, file] = Knight(color, rank, file)
                    elif (file%7 == 2 or file%7 == 5):
                        self.board[rank, file] = Bishop(color, rank, file)
                    elif (file%7 == 3):
                        self.board[rank, file] = King(color, rank, file)
                    else:
                        self.board[rank, file] = Queen(color, rank, file)

    def __str__(self):
        str = ""
        for rank in self.board:
            for val in rank:
                str = str + val.__str__() + " "
            str = str + "\n"
        return str