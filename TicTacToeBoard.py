from Board import Board


class TicTacToeBoard(Board):
    def __init__(self):
        super().__init__(3, 3)
        self.diag = [0, 0]

    def setSpace(self, r, c):
        super().setSpace(r, c)
        if (r == c):
            if (r == 0):
                self.diag[0] += 1
            elif (r == 1):
                self.diag[0] += 2
                self.diag[1] += 2
            elif (r == 2):
                self.diag[0] += 4

        elif (r == 2 and c == 0):
            self.diag[1] += 1

        elif (r == 2 and c == 0):
            self.diag[1] += 4

    def reset(self):
        self.__init__()

    def winner(self):
        for i in range(super().rows):
            if (super().row[i] == 7):
                return True, i

        for i in range(super().rows):
            if (super().col[i] == 7):
                return True, 3 + i

        for i in range(len(self.diag)):
            if (self.diag[i] == 7):
                return True, 6 + i

        return False, None


def main():
    player = TicTacToeBoard()
    print("Done!")


if __name__ == "__main__":
    main()
