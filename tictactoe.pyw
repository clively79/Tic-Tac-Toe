#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from TicTacToeGame import TicTacToeGame


class TicTacToeGUI():
    """The class the governs the TicTacToe GUI environment
    """

    def __init__(self):
        """Constructor class to build the root window and construct the game space
        """
        self.root = Tk()
        self.game = TicTacToeGame()
        self.root.title("Tic-Tac_toe v2.0")
        self.root.resizable(False, False)
        self.root.iconbitmap('tictactoe.ico')
        self.buildMenu()
        self.buildCanvas()
        self.canvas.bind('<1>', self.clickEvent)
        self.root.bind('<Control-n>', lambda e: self.restart())
        self.root.bind('<Control-x>', lambda e: self.root.destroy())
        self.root.mainloop()

    def buildMenu(self):
        self.root.option_add('*tearOff', False)
        self._menubar = Menu(self.root)
        self.root.config(menu=self._menubar)
        self._file = Menu(self._menubar)
        self._mode = Menu(self._menubar)
        self._help = Menu(self._menubar)
        self._menubar.add_cascade(menu=self._file, label='File')
        self._menubar.add_cascade(menu=self._mode, label='Mode')
        self._menubar.add_cascade(menu=self._help, label='Help')
        self._file.add_command(label='New Game', command=self.restart)
        self._file.add_separator()
        self._file.add_command(label='Close', command=self.root.destroy)
        self._file.entryconfig('New Game', accelerator='Ctrl+N')
        self._file.entryconfig('Close', accelerator='Ctrl+X')

    def buildCanvas(self):
        self.canvas = Canvas(self.root, height=300,
                             width=300, background='white')
        self.canvas.create_line(100, 0, 100, 300, width=5, fill='black')
        self.canvas.create_line(200, 0, 200, 300, width=5, fill='black')
        self.canvas.create_line(0, 100, 300, 100, width=5, fill='black')
        self.canvas.create_line(0, 200, 300, 200, width=5, fill='black')
        self.canvas.pack()

    def restart(self):
        """
            Resets reinitializes the TicTacToeGame object
            Destroys the previous canvas and creates a new canvas and 
            recreates the New Game keybinding
        """
        self.game.reset()
        self.canvas.destroy()
        self.buildCanvas()
        self.canvas.bind('<1>', self.clickEvent)

    def clickEvent(self, event):
        """ Displays X/O images on the game space based on where the player clicks 
        and which turn the TicTacToeGame state is in.  

        If the TicTacToeGame Object is in a winning state, calls the winLine method
        to draw a red line of the winning combination.  no further moves will be 
        allowed and the user must create a new game to continue.

        Ctrl-n will start a new game.


        Args:
            event (Object): Bind event properties
        """
        r = event.y // 100
        c = event.x // 100
        if not self.game.occupied(r, c) and not self.game.winner[0]:
            if self.game.turn == 1:
                self.game.select(r, c)
                self.drawX(r, c)

            elif self.game.turn == 2:
                self.game.select(event.y // 100, event.x // 100)
                self.drawO(r, c)

            if self.game.winner[0]:
                self.winLine()

    def drawX(self, r, c):
        x0 = c*100 + 5
        y0 = r*100 + 5
        x1 = c*100 + 95
        y1 = r*100 + 95
        self.canvas.create_line(x0, y0, x1, y1, width=5, fill='black')

        x0 = c*100 + 5
        y0 = r*100 + 95
        x1 = c*100 + 95
        y1 = r*100 + 5
        self.canvas.create_line(x0, y0, x1, y1, width=5, fill='black')

    def drawO(self, r, c):

        x0 = c*100 + 6
        y0 = r*100 + 6
        x1 = x0 + 88
        y1 = y0 + 88
        self.canvas.create_oval(x0, y0, x1, y1, width=5)

    def winLine(self):
        """Draws a red line over the row/column/diagonal indicated in the 
        second item stored in the TicTacToeGame.Winner tuple.  
        """
        if (self.game.winner[1] == 0):
            self.canvas.create_line(5, 50, 295, 50, width=5, fill='red')
        elif (self.game.winner[1] == 1):
            self.canvas.create_line(5, 150, 295, 150, width=5, fill='red')
        elif (self.game.winner[1] == 2):
            self.canvas.create_line(5, 250, 295, 250, width=5, fill='red')
        elif (self.game.winner[1] == 3):
            self.canvas.create_line(50, 5, 50, 295, width=5, fill='red')
        elif (self.game.winner[1] == 4):
            self.canvas.create_line(150, 5, 150, 295, width=5, fill='red')
        elif (self.game.winner[1] == 5):
            self.canvas.create_line(250, 5, 250, 295, width=5, fill='red')
        elif (self.game.winner[1] == 6):
            self.canvas.create_line(5, 5, 295, 295, width=5, fill='red')
        elif (self.game.winner[1] == 7):
            self.canvas.create_line(5, 295, 295, 5, width=5, fill='red')
        self.canvas.pack()


def main():
    TicTacToe = TicTacToeGUI()


if __name__ == "__main__":
    main()
