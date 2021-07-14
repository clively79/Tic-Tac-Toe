class Board():
    """
        A base class for a board style game played on an N x M grid
        in which a player may claim or occupy a space on the board.

        A space may be either claimed or unclaimed.
        when a space is claimed, it's row and column values will be 
        incremented by a power of two.

        diagonal interpolations should be defined in the derived class
        as diagonal behaviors change from game to game. For example,  
        Battleship has no diagonal interperetations, but Tic-Tac-Toe 
        interperets diagonals differently than Connect Four 


    """

    def __init__(self, r, c):
        """Class Constructor

        Args:
            r (Integer): Number of rows on the game Board
            c ([type]): Number of columns on the game board
        """
        self.rows = r
        self.cols = c
        self.row = [0] * self.rows
        self.col = [0] * self.cols
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            self.matrix[i] = [0] * self.cols

    def __repr__(self):
        return str(self.matrix)

    def reset(self):
        """resets the board to its initial state
        """
        self.__init__(self.r, self.c)

    def reset(self, n, m):
        """resets the board to a new configuration
        """
        self.__init__(n, m)

    def setSpace(self, r, c):
        """sets a space on a game board to claimed or occupied only if
            the space is not occupied

        Args:
            r (Integer): Row 
            c (Integer): Column
        """
        if (not self.matrix[r][c]):
            self.matrix[r][c] = 1
            self.row[r] += 2 ** c
            self.col[c] += 2 ** r

    @staticmethod
    def occupied(*args, r, c):
        """
            Static method: Given a list of Board type objects, if the desired row and column
            requested is occupied on any of the boards passed, the method will return true.
            This should be used in any derived class prior to setting a space on a board object
            to avoid any player claiming an already occupied space.

        Args:
            r (Integer): Row 
            c (Integer): Column 

        Returns:
            Boolean:    True Iff none of the Board Objects passed have already claimed the 
                        R/C/ space requested.
        """
        for i in range(len(args)):
            if (args[i].matrix[r][c] == 1):
                return True

        return False
