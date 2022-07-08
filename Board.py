import numpy as np

class Board():
    def __init__(self):
        self.board = np.empty((8,8), dtype=np.str)