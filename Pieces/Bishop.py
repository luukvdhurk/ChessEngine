from Pieces.Piece import Piece

class Bishop(Piece):
    def __init__(self, color, rank, file):
        self.color = color
        self.rank = rank
        self.file = file

    def moveOptions(self, board):
        moveList = []
        # For each direction:
        # Add all positions to the list until you either hit a piece, or hit a border.
        for axis in [(1, 1), (1, -1), (-1, 1)]:
            for direction in [1, -1]:
                original_rank = self.rank
                original_file = self.file
                while (7 >= original_rank + direction * axis[0] >= 0 and
                       7 >= original_file + direction * axis[1] >= 0 and
                       not issubclass(type(board[original_rank + direction * axis[0],
                                                 original_file + direction * axis[1]]), Piece)):
                    moveList.append((original_rank + direction * axis[0], original_file + direction * axis[1]))
                    original_rank = original_rank + direction * axis[0]
                    original_file = original_file + direction * axis[1]

                if (7 >= original_rank + direction * axis[0] >= 0 and
                        7 >= original_file + direction * axis[1] >= 0 and
                        board[original_rank + direction * axis[0],
                              original_file + direction * axis[1]].color != self.color):
                    moveList.append((original_rank + direction * axis[0], original_file + direction * axis[1]))
        return moveList

    def moveTo(self, new_rank, new_file, board):
        board[self.rank, self.file] = None
        board[new_rank, new_file] = self
        self.rank = new_rank
        self.file = new_file

    def __str__(self):
        return self.color + "Bishop"