import Board
import random

class Game():
    def __init__(self):
        self.turn = 0 #White's turn
        self.board = Board.Board()
        self.sides = ["White", "Black"]

    def startGame(self):
        cur_moves = []
        for piece in self.board.board.flatten():
            if piece != None and piece.color == self.sides[self.turn] and len(piece.moveOptions(self.board.board)) > 0:
                cur_moves.append((piece.rank, piece.file, piece.moveOptions(self.board.board)))
        while len(cur_moves) != 0:
            random_piece = random.choice(cur_moves)
            random_move = random.choice(random_piece[2])
            print(random_piece[0], random_piece[1], random_piece[2])
            self.board.board[random_piece[0], random_piece[1]].moveTo(random_move[0], random_move[1], self.board.board)
            print(self.board)
            self.turn = abs(self.turn-1)
            cur_moves = []
            for piece in self.board.board.flatten():
                if piece != None and piece.color == self.sides[self.turn] and len(piece.moveOptions(self.board.board)) > 0:
                    cur_moves.append((piece.rank, piece.file, piece.moveOptions(self.board.board)))