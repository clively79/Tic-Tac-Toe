from Board import Board
from TicTacToeBoard import TicTacToeBoard


class TicTacToeGame():
    def __init__(self):
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
        self.turn, self.nextTurn = self.nextTurn, self.turn

    def reset(self):
        self.__init__()
