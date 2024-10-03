empty_board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def check(board):
  """Function checks if someone won
  Returns x, o or None"""

  # Check each row
  for row in board:
    if row[0] == row[1] == row[2] != 0:
      return row[0]
  
  # Check each column
  for column in range(3):
    if board[0][column] == board[1][column] == board[2][column] != 0:
      return board[0][column]
    
  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] != 0:
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != 0:
    return board[0][2] 

  # Check if at least one empty cell
  for row in range(3):
    for column in range(3):
      if board[row][column] == 0:
        return None
  
    
  return "Tie"


def display_board(board):
  """function displays board in terminal"""
  def character(location, additional_board=False):
    """function returns character to be written in specific location"""
    if board[location[0]][location[1]] == 0:  # If in given board and location value = 0 (return empty)
      if additional_board:
        return str(3 * location[0] + location[1] + 1) # In case of additional board, return cell number
      return " "

    if additional_board:    # If additional block then return empty (not usable)
      return " "
    return board[location[0]][location[1]]  # If location is taken, return x or o

  gap = 20
  print("\n"*30)
  print("   " + character((0, 0)) + " | " + character((0, 1)) + " | " + character((0, 2)) + " " + " " * gap + " "+character((0, 0), 1)+" | "+character((0, 1), 1)+" | "+character((0, 2), 1)+" ")
  print("  ---|---|---" + " " * gap + "---|---|---")
  print("   " + character((1, 0)) + " | " + character((1, 1)) + " | " + character((1, 2)) + " " + " " * gap + " "+character((1, 0), 1)+" | "+character((1, 1), 1)+" | "+character((1, 2), 1)+" ")
  print("  ---|---|---" + " " * gap + "---|---|---")
  print("   " + character((2, 0)) + " | " + character((2, 1)) + " | " + character((2, 2)) + " " + " " * gap + " "+character((2, 0), 1)+" | "+character((2, 1), 1)+" | "+character((2, 2), 1)+" ")
  print()


def insert_character(board, location, character):
  """Function inserts character in board list at provided location (1-9)"""
  
  location = int(location) - 1
  row = location//3
  col = location - 3 * (location//3)

  if board[row][col] != 0:
    return False                                   # If location already occupied, return False

  board[row][col] = character
  return board                                      # Once operation done, return new board (doesn't matter)


def copyList(originalList):
  output = []
  for i in range(len(originalList)):
    tmp = []
    for element in originalList[i]:
      tmp.append(element)
    output.append(tmp)

  return output


def available_cells(board):
  """Function returns list of available moves"""
  
  cells = []
  i = 0
  for row in range(3):
    for column in range(3):
      i += 1
      if board[row][column] == 0:
        cells.append(i)
  return cells


def minimax(board, char, maxTurn):
  """Minimax algorithm function"""
  
  if char == "x":
    next_char = "o"
  else:
    next_char = "x"

  # Base case
  if check(board) == "Tie":
    score = 0
    return score, 0
  elif check(board) == char:
    score = maxTurn
    return score, 0
  elif check(board) == next_char:
    score = -maxTurn
    return score, 0


  available_moves = available_cells(board)
  
  scores = []

  for selected_move in available_moves:
    next_board = insert_character(copyList(board), selected_move, char)

    score, move = minimax(next_board, next_char, -maxTurn)
    scores.append([score, selected_move])

  if maxTurn == 1:
    return max(scores)
  else:
    return min(scores)


def play(board, computer=False, computer_char=None):
  char_turn = "o"
  while True:
    if char_turn == "o":
      char_turn = "x"
    else:
      char_turn = "o"

    display_board(board)

    board_result = check(board)
    if board_result != None:          # Game has finished
      if board_result == "Tie":
        print("It was a tie this game, nobody won :/")
        break

      print(board_result + " won this game, congratulations " + board_result)
      break

    print("Available moves: ", available_cells(board))

    if computer and char_turn == computer_char:      # Check if computer turn
      best_score, best_move = minimax(board, char_turn, 1)
      
      insert_character(board, best_move, char_turn)


      continue # Skip player move

    valid_input = False
    while not valid_input:
      input_location = input("It is " + char_turn + " turn: ")

      res = insert_character(board, input_location, char_turn)

      if res != False:
        board = res
        valid_input = True



while True:
  print("\n\n")

  computer = input("Do you want to play against a computer? : ")
  if computer == "yes":
    human_char = input("What character do you want to play with x / o : ")
    if human_char == "o":
      computer_char = "x"
    else:
      computer_char = "o"

    play(copyList(empty_board), True, computer_char)

  else:
    play(copyList(empty_board))
