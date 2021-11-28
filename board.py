board = ['-','-','-',
         '-','-','-',
         '-','-','-']
game_continues = True
player_one = "X"
def show_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
def game_start():
    show_board()
    while game_continues:
        place_mark(player_one)
        player_swap()

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

game_start()

