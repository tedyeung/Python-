from IPython.display import clear_output

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
        print ('Wrong input please try again!!')
        marker = input("Player One: Do you want to be X or O").upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')
player_input()