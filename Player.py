"""
        A Class representing a player in a game of tic-tac-toe

        Fields:
            Int     _n      stores the number of rows and columns
                            integer values 3 >= _width <= 9
            List    _board  array of binary values 0/1 zero is an open space,
                            one is an occupied space.
            List    _rows   Each element of _row[i] is a reference to the
                            corresponding values in the _board List below. If the
                            binary string representation of a row = 2^(_n),
                            the player has a winning row.

                            for all i = [0 .. n-1]
                                _row[i] = _board[i*n .. (i+1)*n-1]

            List    _cols   Each element of _col[i] is a reference to the
                            corresponding values in the _board List below. If the
                            binary string representation of a column = 2^(_n),
                            the player has a winning row.

                            for all i = [0 .. n-1]
                                _col[i] = _board[1:n-1:n]


"""


def main():

    B = list(range(0, 3))
    C = list(range(3, 6))
    D = list(range(6, 9))
    A = [B, C, D]
    A = "".join(map(int, A))
    print(A)


if __name__ == "__main__":
    main()
