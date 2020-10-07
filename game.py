# Tic Tac Toe Game Written in Python

# Global Variables
board_size=3
game_over=False

# I need a 3x3 board
board=list(range(1, pow(board_size, 2)+1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create board dynamically 
board_2d=[]

for x in range(0, board_size):
  board_2d.append(board[slice(board_size*x, board_size*x+board_size)])

def define_board():
  global board_size
  # Get user to enter the board size they want to play
  print("\nEnter a number to define the board size \ne.g. 4 for 4x4 \nIf no value is entered, the default will be 3x3")

  board_size = 3 if input() == '' else input()

# Display the board
def display_board():
    # Prints out the 2d array called board_2d into a board
    for row in board_2d:
      for col in row:
        print(col, end=' ')

         # Check if the column is the last element in the first row
        if row.index(col) != len(row)-1:
            # Not the last element
            print(' | ', end=' ')
        else:
            # Its the last element, now check if it is the row is the last element in the board
            if board_2d.index(row) != len(board_2d)-1:
                divider='-'* board_size * 5
                print('\n'+divider)


# Flip player
def switch_player_turn(turn):
    if turn=="player1":
        return "player2"
    else:
        return "player1"


# Handle Player's turn
def get_player_move(turn):
    global board
    
    print("\n"+turn[0]+" choose a box to place an '"+turn[1]+"' into:", end="\n")
    player_input=input()
    board_index=int(player_input)-1
    # Check if the position has been occupied
    if(isinstance(board[board_index], int)):
    board[board_index]=turn[1]
    display_board()
    check_for_win(board, turn)
    else:
      print('Position '+str(player_input)+' has been filled, please choose another position.')
      get_player_move(turn)


# Check win, row, columns, diagonal
def check_for_win(board, player):
    mark=player[1]
    global game_over
    if(
        (board[0] == board[1] == board[2] == mark) or
        (board[3] == board[4] == board[5] == mark) or
        (board[6] == board[7] == board[8] == mark) or
        (board[0] == board[3] == board[6] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[0] == board[4] == board[8] == mark) or
        (board[2] == board[4] == board[6] == mark)
        ):
        print("\nCongratulations "+player[0]+"! You have won.")
        game_over=True
    else:
        game_over=False


# Launch play game
def play_game():
    # First, get players name
    print("\nEnter name for Player 1")
    name_player1=input()
    print("\nEnter name for Player 2")
    name_player2=input()
    global game_over

    # Second, store player's name into the value pair of the respective key
    players={
        "player1":[name_player1, 'x'],
        "player2":[name_player2, 'o']
    }
    
    # Third, set up player 1 starts first
    turn="player1"

    # Fourth, get user to define the board size
    define_board()
    
    # Fifth, display the tic tac toe board
    display_board()
    
    # Finally, run the game continuously if game is not over(aka no winner)
    while not game_over:
        # Get player move position, show move and check for win
        get_player_move(players[turn])
        # Switch player
        turn=switch_player_turn(turn)
    

# Run the game
play_game()
