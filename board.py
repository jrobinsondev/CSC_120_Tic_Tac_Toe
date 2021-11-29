board = ['-','-','-',
         '-','-','-',
         '-','-','-']
game_continues = True
player_one = "X"
winner = None
def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def game_start():
    show_board()
    while game_continues:
        place_mark(player_one)
        game_condition()
        player_swap()
    if winner == "X" or winner == "O":
        print(winner + " is the winner.")
    elif winner == None:
        print("It's a draw!")
def place_mark(player):
    print(player + "'s turn.")
    position = input("Place a mark from 1-9:")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Place a mark from 1-9:")
            print("Error, position not in range.")
        position = int(position) - 1
        if board[position] == "-":
            valid = True
        else:
            print("Position already filled, choose another spot.")
    board[position] = player
    show_board()
def player_swap():
    global player_one
    if player_one == "X":
        player_one = "O"
    elif player_one == "O":
        player_one = "X"
def game_condition():
    winner_check()
    tie_check()

def winner_check():
    global winner
    row_win = row_check()
    column_win = column_check()
    diag_win = diag_check()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diag_win:
        winner = diag_win
    else:
        winner = None
def row_check():
    global game_continues
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_continues = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None
def column_check():
    global game_continues
    column_1 = board[0] == board[1] == board[2] != "-"
    column_2 = board[3] == board[4] == board[5] != "-"
    column_3 = board[6] == board[7] == board[8] != "-"
    if column_1 or column_2 or column_3:
        game_continues = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None
def diag_check():
    global game_continues
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_continues = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]
    else:
        return None

def tie_check():
    global game_continues
    if "-" not in board:
        game_continues = False
        return True
    else:
        return False

game_start()


