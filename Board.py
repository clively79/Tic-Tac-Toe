from Space import Space
from math import sqrt


class Board():

    def __init__(self, n):
        self.p = int(sqrt(n))
        self.sp = []
        self.row = []
        self.col = []
        self.diags = []

        for i in range(0, n):
            self.sp.append(Space())

        for i in range(0, self.p):
            self.row.append(self.sp[i*self.p:(i+1)*self.p])
            self.col.append(self.sp[i:n:self.p])

        self.diags.append(self.sp[0:n:self.p+1])
        self.diags.append(self.sp[self.p-1:n-(self.p-1):self.p-1])
        self.diags[1].reverse()

    def __repr__(self):
        return str(self.sp)

    def __str__(self):
        return str(self.sp)

    def printBoard(self):
        print(*self.sp, sep="")

    def set(self, n):
        self.sp[n].set()

    def reset(self, n):
        for i in range(0, n):
            self.sp[i].reset()

    def binToDecimal(self, s):
        dval = 0
        rlist = list(s)
        rlist.reverse()
        rString = ''.join(map(str, rlist))
        for i, v in enumerate(rString):
            if(v == "1"):
                dval += 2**i

        return dval

    def winner(self):

        for i in range(len(self.row)):
            if self.binToDecimal(''.join(map(str, self.row[i]))) == 7:
                return True, i

        for i in range(len(self.col)):
            if self.binToDecimal(''.join(map(str, self.col[i]))) == 7:
                return True, i+self.p

        for i in range(len(self.diags)):
            if self.binToDecimal(''.join(map(str, self.diags[i]))) == 7:
                return True, i+(2 * self.p)

        return False, None


# def main():
#     board = Board(9)
#     board.set(0)
#     # board.set(1)
#     # board.set(2)
#     # board.set(3)
#     board.set(4)
#     # board.set(5)
#     # board.set(6)
#     # board.set(7)
#     board.set(8)

#     winner = board.winner()
#     if winner[0]:
#         print(f"winner found on {winner[1]}")
#     board.reset(9)
#     board.printBoard()


# main()
