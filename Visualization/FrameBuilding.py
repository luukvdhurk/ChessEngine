import tkinter
from tkinter import *

class FrameBuilding():
    def __init__(self, board):
        ## Generate the board
        self.blackWhite = ["brown", "white"]
        self.window = Tk()
        self.window.title("Chess Engine")
        self.window.geometry("1300x700")
        self.canvas = Canvas(self.window, width=610, height=610)

        for rank in range(len(board)):
            for file in range(len(board[rank])):
                offset = 25
                squareSize = 70
                self.canvas.create_rectangle(offset+rank*squareSize,offset+file*squareSize,offset+(rank+1)*squareSize, offset+(file+1)*squareSize, fill=self.blackWhite[(rank+file+1)%2], outline="black")
        ## Generate the pieces

        for rank in range(len(board)):
            for file in range(len(board[rank])):
                offset = 35
                squareSize = 70
                ## Top, so the black pieces
                if(file == 0 | file == 1):
                    self.canvas.create_text(offset+rank*squareSize, offset+file*squareSize, text="BP")
                ## If not the case, white pieces
                else:
                    pass
        self.canvas.pack()
        self.window.mainloop()