TicTacToe game based on console written in python.


There are 2 game modes:
  1. local player vs player
  2. player vs computer

Computer is programmed to choose best moves based on minimax algorithm. Minimax algorithm is written using recursive function.


Once run, console will promt if you'd like to play against computer, if you wish to play against computer type "yes" and then select which character to play as (x or o).
If wish to play locally human vs human, then write anything else in the promt, and game will start by asking X move first.

Playing game is simple. Console will be displaying 2 board, the left board is playing board, the right board will show available cells (and their corresponding number) which player can choose.

At the end of the game winner will be announced (or tell that it is a tie in case no-one won) and initial prompt to play against computer will be asked.

There are many optimisations that could be added to minimax algorithm to make it faster and more efficient, but my goal was to make tic tac toe computer impossible to win.
