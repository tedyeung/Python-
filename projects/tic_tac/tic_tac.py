print ('WELCOME TO TIC TAC TOE GAME ENJOY')
print ('**********************************')

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def tic_tac_board (board):
    print (' ' + board[1] + '|' + board[2] + '|' + board[3] + " ")
    print (' ' + " " + '|' + " " + '|' + " " + " ")
    print ('___________')
    print (' ' + board[4] + '|' + board[5] + '|' + board[6] + " ")
    print (' ' + " " + '|' + " " + '|' + " " + " ")
    print ('___________')
    print (' ' + board[7] + '|' + board[8] + '|' + board[9] + " ")
    print (' ' + " " + '|' + " " + '|' + " " + " ")
    print ('**********************************')


tic_tac_board(board)