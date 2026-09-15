"""
Tic-Tac-Toe (2 player, terminal-based)

A simple command-line tic-tac-toe game for two human players. The board is
represented as a list of 9 cells. Players take turns entering a move
(1-9), and the game checks for a winner or a tie after each move.

"""

WINNING_LINES = [
    (0, 1, 2),  # top row
    (3, 4, 5), # middle row
    (6, 7, 8), # bottom row
    (0, 3, 6),  # first col
    (1, 4, 7),  # middle col
    (2, 5, 8),  # last col
    (0, 4, 8),  # LTR diag
    (2, 4, 6),  # RTL diag
]

def create_board():
    return [' '] * 9

def print_board(board):
    print('|'.join(board[0:3]))
    print('---------')
    print('|'.join(board[3:6]))
    print('---------')
    print('|'.join(board[6:9]))

def has_won(board, player):
    for combo in WINNING_LINES:
        slot1,slot2,slot3 = combo
        if board[slot1] == player and board[slot2] == player and board[slot3] == player:
            return True
    return False

def is_full(board):
    return ' ' not in board

def make_move(board, player):
    while True:
        input_value = input(f"Player {player}, enter your move 1-9:")
        try:
            #I use 0-index for input but wanted to make input user-friendly
            move = int(input_value) - 1
        except ValueError:
            print("This is not a valid number. Try again")
            continue
        if(move < 0 or move > 8):
            print("This number is outside of accepted range. Try again.")
            continue
        if(board[move] != ' '):
            print("This slot has already been used. Try again.")
            continue
        else:
            return move
        
def play_game():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        move = make_move(board,current_player)
        board[move] = current_player
        if(has_won(board, current_player)):
            print(f"Player {current_player} has won the game")
            break
        if(is_full(board)):
            print("All slots have been fulled resulting in a tie game. Play Again?")
            break
        if(current_player == 'X'):
            current_player = 'O'
        else:
             current_player = 'X'       