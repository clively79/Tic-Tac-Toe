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
        self.rows = r
        self.cols = c
        self.row = [0] * self.r
        self.col = [0] * self.c
        self.matrix = []
        for i in range(self.rows):
            self.matrix.append([])
            self.matrix[i] = [0] * self.cols

    def __repr__(self):
        return str(self.matrix)

    def reset(self):
        self.__init__(self.r, self.c)

    def setSpace(self, r, c):
        if (not self.matrix[r][c]):
            self.matrix[r][c] = 1
            self.row[r] += 2 ** c
            self.col[c] += 2 ** r

    @staticmethod
    def occupied(*args, r, c):
        for i in range(len(args)):
            if (args[i].matrix[r][c] == 1):
                return True
