from random import randint
 
#If 1, display the guess of the computer for testing
COMPUTER_GUESS=0
#Number of guesses allowed
NO_USER_GUESS=4
 
board = []
 
#Create a 5x5 2 dimensional list
for x in range(5):
    board.append(["O"] * 5)
 
def print_board(board):
    print ("Battleship field")
    print ("================")
    for row in board:
        print (" ".join(row))
 
print ("=" * 50)
print ("- Let's play Battleship!")
print ("- Take a guess between 0 and 4 for row & column")
print ("- You have " + str(NO_USER_GUESS) + " turns to complete the game")
print ("=" * 50 + "\n")
print_board(board)
 
def random_row(board):
    return randint(0, len(board) - 1)
 
def random_col(board):
    return randint(0, len(board[0]) - 1)
 
ship_row = random_row(board)
ship_col = random_col(board)
 
if COMPUTER_GUESS == 1:
  print ("Computer guessed row: %d column: %d" % (ship_row,ship_col))
 
turn = 0
for attempt in range(NO_USER_GUESS):
  print ("\n")
  guess_row = int(input("Guess Row:"))
  guess_col = int(input("Guess Col:"))
 
  if guess_row == ship_row and guess_col == ship_col:
      print ("Congratulations! You sunk my battleship!")
      break
  else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
          print ("Oops, that's not even in the ocean.")
      elif(board[guess_row][guess_col] == "X"):
          print ("You guessed that one already!!!")
      else:
          print ("You missed my battleship!")
          board[guess_row][guess_col] = "X"
 
      print ("Turn %d \n" % (turn + 1)) 
      print_board(board)
      turn = turn + 1
      
      if turn == NO_USER_GUESS:
          print ("Game Over")
