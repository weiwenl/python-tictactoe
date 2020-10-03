# Tic Tac Toe Game Written in Python

# Global Variables
board_size=3
game_over=False

# I need a 3x3 board
board=list(range(1, pow(board_size, 2)+1)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Display the board
def display_board():
    print("\n")
    print(str(board[0])+" | "+str(board[1])+" | "+str(board[2]))
    print("--------")
    print(str(board[3])+" | "+str(board[4])+" | "+str(board[5]))
    print("--------")
    print(str(board[6])+" | "+str(board[7])+" | "+str(board[8]))


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
    board_index=int(input())-1
    board[board_index]=turn[1]
    display_board()
    check_for_win(board, turn)


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

    # Fourth, display the tic tac toe board
    display_board()
    
    # Finally, run the game continuously if game is not over(aka no winner)
    while not game_over:
        # Get player move position, show move and check for win
        get_player_move(players[turn])
        # Switch player
        turn=switch_player_turn(turn)
    

# Run the game
play_game()
