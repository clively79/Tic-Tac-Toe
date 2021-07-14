from Board import Board
from TicTacToeBoard import TicTacToeBoard


class TicTacToeGame():
    """
        A Wrapper class to manage the flow and procedure of a
        player v. player TicTacToe game designed to be implemented 
        in a GUI environment 
    """

    def __init__(self):
        """Constructor
        """
        self.player1 = TicTacToeBoard()
        self.player2 = TicTacToeBoard()
        self.turn = 1
        self.nextTurn = 2
        self.movesRemaining = 9
        self.winner = (False, None)
        self.draw = False

    def __repr__(self):
        return "TicTacToeGame"

    def select(self, r, c):
        """Selects a space on the game board for the current players turn


        Args:
            r (Integer): The Row the player chooses
            c (Integer): The column the player chooses
        """
        if (not Board.occupied(self.player1, self.player2, r=r, c=c)):
            if (self.turn == 1):
                self.player1.setSpace(r, c)
                self.winner = self.player1.winner()
                if (not self.winner[0]):
                    self.swapTurns()
                    self.movesRemaining -= 1

            elif(self.turn == 2):
                self.player2.setSpace(r, c)
                self.winner = self.player1.winner()
                if (not self.winner[0]):
                    self.swapTurns()
                    self.movesRemaining -= 1

        if(self.movesRemaining == 0 and not self.winner[0]):
            self.draw = True

    def swapTurns(self):
        """Helper method to swap the which players will go next
        """
        self.turn, self.nextTurn = self.nextTurn, self.turn

    def reset(self):
        """Resets the game to its initial state.
        """
        self.__init__()
