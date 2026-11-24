"""
Tic-Tac-Toe (1 or 2 player, terminal-based)

A simple command-line tic-tac-toe game for one human player and a computer or 2 humans. 
The board is represented as a list of 9 cells. Players take turns entering a move
(1-9), and the game checks for a winner or a tie after each move.

"""
import random

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

def get_empty_spaces(board):
    return [i for i in range(9) if board[i] == ' ']

def random_move(board):
    return random.choice(get_empty_spaces(board))

def get_best_move(board, player):
    #optimize to always take center
    empty_spaces = get_empty_spaces(board)
    if(len(empty_spaces) == 8):
        if(board[4]== ' '):
            return 4
        else:
            return random_move(board)
    #test my potential win
    for space in empty_spaces:
        board[space] = player
        if(has_won(board,player)):
            board[space] = ' '
            return space
        board[space] = ' '
    #test oppo win
    for space in empty_spaces:
        board[space] = 'X'
        if(has_won(board, 'X')):
            board[space] = ' '
            return space
        board[space] = ' '
    #make decision if not either
    return random_move(board)

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

def choose_game_mode():
    while True:
        choice = input("Choose mode: 1 for one-player (vs computer), 2 for two-player: ")
        try:
            game_mode= int(choice)
        except ValueError:
            print("This is not a valid number. Try again")
            continue  
        if game_mode < 1 or game_mode > 2:
            print("This number is not a valid choice. Try again.")
            continue
        if game_mode == 1:
            return True
        else:
            return False

def play_game():
    board = create_board()
    current_player = 'X'
    one_player = choose_game_mode()

    while True:
        print_board(board)
        if (current_player == 'O'):
            if one_player == False :
                move = make_move(board,current_player)
            else:
                move = get_best_move(board, current_player)
        else:     
            move = make_move(board,current_player)
        board[move] = current_player
        if(has_won(board, current_player)):
            print(f"Player {current_player} has won the game")
            print_board(board)
            break
        if(is_full(board)):
            print("All slots have been filled resulting in a tie game.")
            print_board(board)
            break
        if(current_player == 'X'):
            current_player = 'O'
        else:
             current_player = 'X'       

def ask_to_play_again():
    while True:
        try:
            answer = input("Play Again? (y/n): ")
        except EOFError:
            print()
            return False
        answer = answer.strip().lower()
        if answer in ('y', 'yes'):
            return True
        if answer in ('n', 'no'):
            return False
        print("Please enter yes or no.")

def main():
    while True:
        play_game()
        if not ask_to_play_again():
            break

if __name__ == '__main__':
    main()
