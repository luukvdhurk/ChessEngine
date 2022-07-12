from Pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file
        self.move_direction = 1 if (self.color == "White") else -1

    def moveOptions(self, board):
        moveList = []

        if (7 >= self.rank + self.move_direction >= 0):
            if (board[self.rank + self.move_direction, self.file] == None):
                #Regular forward movement
                moveList.append((self.rank + self.move_direction, self.file))
            else:
                for direction in [-1, 1]:
                    #Diagonal capturing movement
                    if (7 >= self.file + direction >= 0 and
                            issubclass(type(board[self.rank + self.move_direction, self.file + direction]), Piece) and
                            board[self.rank + self.move_direction, self.file + direction].color != self.color):
                        moveList.append((self.rank + self.move_direction, self.file + direction))


        return moveList

    def moveTo(self, new_rank, new_file, board):
        board[self.rank, self.file] = None
        board[new_rank, new_file] = self
        self.rank = new_rank
        self.file = new_file

        pass

    def __str__(self):
        return self.color + "Pawn"
