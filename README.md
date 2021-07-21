# Tic-Tac-Toe
To run:  associate .pyw file extentions with the pythonw executable and doubleclick, or type `pythonw tictactoe.py` in commandline. This will suppress the python console window.  you can use the python interpereter to run as well, but this will not supress the python console.

This is a work in progress and additonal features are comming.  For now,  to restart a game,  press ctrl-n any time.

A simple Tic-Tac-Toe program, created to exercise some fundamental Python concepts.

  I'm Learning python, and I figured creating a simple Tic-Tac-Toe game using object oriented design principals would be an excelent way to learn the language.  This program will use a GUI to setup the game board and a wrapper class to manage the game state and flow.  

  The wrapper class contains a TicTacToe game board for each player, and the first player to complete a row, column or diagonal wins. To minimize memory consumption,  each row, column and diagonal is represented by the sum of powers of two.  this allows for only one unique value for each possible configuration of a players row, and also reduces the number of comparisons and loops needed to verify a particular state. 
    
  For example:  a player's row which contains ` X |  | X ` would have a total of the leftmost X earnes a value of 2^0 (1) and the rightmost X earns a value of 2^2 (4).     If the player were to claim the middle space, the row total would earn another 2^1 points bringing it to a sum of 7 which can easily identify a winner without         additional loops and comparisons. This method can easily be expanded to other games and scale to games requiring a larger game board dimention and automatically       scale the row and column dimentions.

  the TicTacToe game board is derived from a generic M x N game board class that can be used to derive other board games in which a single occupies a space on a game board.  Diagonals are not defined by the parent Board class, because different games handle diagonals differently.  In any variation of Tic-Tac-Toe,  there are only two diagonals, regardless of the number of rows/columns. Connect Four has a lattice of diagonals, which only require four consecutive, rather than a completed diagonal. Battleship has no diagonals.
