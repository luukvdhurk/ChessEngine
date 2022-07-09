import Board
from Visualization.FrameBuilding import FrameBuilding

board = Board.Board()
frame = FrameBuilding(board.board)
old_rank = 1
old_file = 1
for i in range(0,6):
    new_rank, new_file = board.board[old_rank, old_file].moveOptions(board.board)[0]
    board.board[old_rank, old_file].moveTo(new_rank, new_file, board.board)
    old_rank = new_rank
    old_file = new_file
    print(board)