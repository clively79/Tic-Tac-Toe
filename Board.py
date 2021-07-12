from Space import Space
from math import sqrt


class Board():
    """
        A class used to represent a square two dimential game board.
        A player's board consists for a list of Space objects in row major
        order.  each space may contain a value of 0 if unocupied and 1 if
        occupied.
    """

    def __init__(self, n):
        """Constructor

        Args:
            n (Integer): number of rows
        """
        self.p = n ** 2
        self.sp = []
        self.row = []
        self.col = []
        self.diags = []

        for i in range(0, self.p):
            self.sp.append(Space())

        for i in range(0, n):
            self.row.append(self.sp[i*n:(i+1)*n])
            self.col.append(self.sp[i:self.p:n])

        self.diags.append(self.sp[0:self.p:n+1])
        self.diags.append(self.sp[n:self.p:n-1])
        self.diags[1].reverse()

    def __repr__(self):
        return str(self.sp)

    def __str__(self):
        return str(self.sp)

    def set(self, n):
        """ Setter method, changes the state of the desired space from 0 (unoccupied)
            to 1 (occupied).

        Args:
            n (Integer): Index of the space chosen by the player
        """
        self.sp[n].set()

    def reset(self):
        """Resets all the player's spaces to 0 (unoccupied)

        """
        for i in range(0, self.p):
            self.sp[i].reset()

    def _binToDecimal(self, s):
        """Helper method: Accepts a binary string converts decimal value

        Args:
            s (String): Binary coded decimal

        Returns:
            Integer: integer value omputed from binary coded decimal s
        """
        dval = 0
        rlist = list(s)
        rlist.reverse()
        rString = ''.join(map(str, rlist))
        for i, v in enumerate(rString):
            if(v == "1"):
                dval += 2**i

        return dval

    def winner(self):
        """Determines if the player's board contains a winning row, column, or diagonal

        Returns:
            Tuple: (Boolean, integer)
        """
        for i in range(len(self.row)):
            if self._binToDecimal(''.join(map(str, self.row[i]))) == 7:
                return True, i

        for i in range(len(self.col)):
            if self.binToDecimal(''.join(map(str, self.col[i]))) == 7:
                return True, i+self.p

        for i in range(len(self.diags)):
            if self.binToDecimal(''.join(map(str, self.diags[i]))) == 7:
                return True, i+(2 * self.p)

        return False, None
