from Board import Board


class TicTacToeBoard(Board):
    """ Class TicTacToeBoard, inherits Board adds diagonals for identifying winners
        Creates a 3x3 board consisting of 3 rows, 3 columns and 2 diagonals

        When all three spaces in a board are claimed their value = 7

            row[n] = [X][X][X] = 1+2+4 = 7

        Each claimed space adds a power of 2^c

        Column and Diagonal values are similarly computed  

    Args:
        Board (Class): Base class
    """

    def __init__(self):
        """
            Constructor: creates a 3x3 TicTacToe board
        """
        super().__init__(3, 3)
        self.diag = [0, 0]

    def setSpace(self, r, c):
        """
            Claims a space on the board, setting row, column and diagonal values
            If the space on the board in already occupied,  no action is taken

        Args:
            r (Integer): Desired row index beginning at 0
            c (Integer): Disired column index beginning at 0
        """
        if(not self.matrix[r][c]):
            super().setSpace(r, c)
            if (r == c):
                if (r == 0):
                    self.diag[0] += 1
                elif (r == 1):
                    self.diag[0] += 2
                    self.diag[1] += 2
                elif (r == 2):
                    self.diag[0] += 4

            elif (r == 0 and c == 2):
                self.diag[1] += 4

            elif (r == 2 and c == 0):
                self.diag[1] += 1

    def reset(self):
        """
            Resets the board to it's initial state
        """
        self.__init__()

    def winner(self):
        """ 
            Determines in a game board is in a winning state
            if the game board is not in a winning state, returns (False, None)

            if the game board is in a winning state returns (True, Int) where
                int 0 = winner on Row 1
                int 1 = winner on Row 2
                int 2 = winner on Row 3
                int 3 = winner on Column 1
                int 4 = winner on Column 2
                int 5 = winner on Column 3
                int 6 = winner on Diagonal 1
                int 7 = winner on Diagonal 2
        Returns:
            Tuple: (Boolean, Integer)
        """
        for i in range(self.rows):
            if (self.row[i] == 7):
                return True, i

        for i in range(self.rows):
            if (self.col[i] == 7):
                return True, 3 + i

        for i in range(len(self.diag)):
            if (self.diag[i] == 7):
                return True, 6 + i

        return False, None


def main():
    player = TicTacToeBoard()
    player.setSpace(2, 0)
    player.setSpace(1, 1)
    player.setSpace(0, 2)
    print(player.winner())
    player.reset()
    print("Done!")


if __name__ == "__main__":
    main()
