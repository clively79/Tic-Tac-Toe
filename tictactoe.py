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
        self.root.geometry('310x310+50+50')
        self.root.resizable(False, False)
        self.root.iconbitmap('tictactoe.ico')
        self.O_image = PhotoImage(file='o.gif')
        self.X_image = PhotoImage(file='x.gif')
        self.canvas = Canvas(self.root, height=310,
                             width=310, background='white')
        self.canvas.create_line(103, 0, 103, 310, width=5, fill='black')
        self.canvas.create_line(208, 0, 208, 310, width=5, fill='black')
        self.canvas.create_line(0, 103, 310, 103, width=5, fill='black')
        self.canvas.create_line(0, 208, 310, 208, width=5, fill='black')
        self.canvas.pack()
        self.canvas.bind('<1>', self.clickEvent)
        self.root.bind('<Control-n>', lambda e: self.restart())
        self.root.mainloop()

    def restart(self):
        """
            Resets reinitializes the TicTacToeGame object
            Destroys the previous canvas and creates a new canvas and 
            recreates the New Game keybinding
        """
        self.game.reset()
        self.canvas.destroy()
        self.canvas = Canvas(self.root, height=310,
                             width=310, background='white')
        self.canvas.create_line(103, 0, 103, 310, width=5, fill='black')
        self.canvas.create_line(208, 0, 208, 310, width=5, fill='black')
        self.canvas.create_line(0, 103, 310, 103, width=5, fill='black')
        self.canvas.create_line(0, 208, 310, 208, width=5, fill='black')
        self.canvas.pack()
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
        if (event.y <= 100 and not self.game.winner[0]):
            if (event.x <= 100):
                if (not self.game.occupied(0, 0)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            0, 0, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            0, 0, image=self.O_image, anchor='nw')
                    self.game.select(0, 0)
                    self.canvas.pack()

            elif (event.x <= 205):
                if (not self.game.occupied(0, 1)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            105, 0, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            105, 0, image=self.O_image, anchor='nw')
                    self.game.select(0, 1)
                    self.canvas.pack()

            elif (event.x <= 310):
                if (not self.game.occupied(0, 2)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            210, 0, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            210, 0, image=self.O_image, anchor='nw')
                    self.game.select(0, 2)
                    self.canvas.pack()

        elif (event.y <= 205 and not self.game.winner[0]):
            if (event.x <= 100):
                if (not self.game.occupied(1, 0)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            0, 105, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            0, 105, image=self.O_image, anchor='nw')
                    self.game.select(1, 0)
                    self.canvas.pack()

            elif (event.x <= 205):
                if (not self.game.occupied(1, 1)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            105, 105, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            105, 105, image=self.O_image, anchor='nw')
                    self.game.select(1, 1)
                    self.canvas.pack()

            elif (event.x <= 310):
                if (not self.game.occupied(1, 2)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            210, 105, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            210, 105, image=self.O_image, anchor='nw')
                    self.game.select(1, 2)
                    self.canvas.pack()

        elif (event.y <= 310 and not self.game.winner[0]):
            if (event.x <= 100):
                if (not self.game.occupied(2, 0)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            0, 210, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            0, 210, image=self.O_image, anchor='nw')
                    self.game.select(2, 0)
                    self.canvas.pack()

            elif (event.x <= 205):
                if (not self.game.occupied(2, 1)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            105, 210, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            105, 210, image=self.O_image, anchor='nw')
                    self.game.select(2, 1)
                    self.canvas.pack()

            elif (event.x <= 310):
                if (not self.game.occupied(2, 2)):
                    if (self.game.turn == 1):
                        self.canvas.create_image(
                            210, 210, image=self.X_image, anchor='nw')
                    elif(self.game.turn == 2):
                        self.canvas.create_image(
                            210, 210, image=self.O_image, anchor='nw')
                    self.game.select(2, 2)
                    self.canvas.pack()

        if self.game.winner[0]:
            self.winLine()

    def winLine(self):
        """Draws a red line over the row/column/diagonal indicated in the 
        second item stored in the TicTacToeGame.Winner tuple.  
        """
        if (self.game.winner[1] == 0):
            self.canvas.create_line(5, 50, 305, 50, width=5, fill='red')
        elif (self.game.winner[1] == 1):
            self.canvas.create_line(5, 155, 305, 155, width=5, fill='red')
        elif (self.game.winner[1] == 2):
            self.canvas.create_line(5, 260, 305, 260, width=5, fill='red')
        elif (self.game.winner[1] == 3):
            self.canvas.create_line(50, 5, 50, 305, width=5, fill='red')
        elif (self.game.winner[1] == 4):
            self.canvas.create_line(155, 5, 155, 305, width=5, fill='red')
        elif (self.game.winner[1] == 5):
            self.canvas.create_line(260, 5, 260, 305, width=5, fill='red')
        elif (self.game.winner[1] == 6):
            self.canvas.create_line(5, 5, 305, 305, width=5, fill='red')
        elif (self.game.winner[1] == 7):
            self.canvas.create_line(5, 305, 305, 5, width=5, fill='red')
        self.canvas.pack()


def main():
    TicTacToe = TicTacToeGUI()


if __name__ == "__main__":
    main()
