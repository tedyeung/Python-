print ('WELCOME TO TIC TAC TOE GAME ENJOY')
print ('**********************************')
print ('                                  ')

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

def tic_tac_board (board):
    print (' ' + board[1] + '|' + board[2] + '|' + board[3] + " ")
    print ("--------")
    print (' ' + board[4] + '|' + board[5] + '|' + board[6] + " ")
    print ('--------')
    print (' ' + board[7] + '|' + board[8] + '|' + board[9] + " ")
    print ('                                  ')
    print ('**********************************')


tic_tac_board(board)

player_one = 'X'
player_two = 'O'

def input_player():
    input_ppl = input('Please choose X or O: ')
    input_ppl = input_ppl.upper()
    return input_ppl
print(input_player())
