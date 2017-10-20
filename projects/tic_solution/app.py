from IPython.display import clear_output
import random

def display_board(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | '  + board[2] + ' | ' + board[3])


board = ['X']*10
display_board(board)

def player_input():
    marker = ''
    while not (marker == 'O' or marker == "X"):
        marker = input("Player One: Do you want to be X or O: ").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
player_input()

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or    
    (board[1] == mark and board[2] == mark and board[3] == mark) or  
    (board[7] == mark and board[4] == mark and board[1] == mark) or   
    (board[8] == mark and board[5] == mark and board[2] == mark) or     
    (board[9] == mark and board[6] == mark and board[3] == mark) or      
    (board[7] == mark and board[5] == mark and board[3] == mark) or     
    (board[9] == mark and board[5] == mark and board[1] == mark)     )

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

