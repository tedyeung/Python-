print ('WELCOME TO TIC TAC TOE GAME ENJOY')
print ('**********************************')
print ('                                  ')

board = [" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 ", " 7 ", " 8 ", " 9 ", " 10 "]

def tic_tac_board (board):
    print (' ' + board[1] + '|' + board[2] + '|' + board[3] + " ")
    print ("-------------")
    print (' ' + board[4] + '|' + board[5] + '|' + board[6] + " ")
    print ('--------------')
    print (' ' + board[7] + '|' + board[8] + '|' + board[9] + " ")
    print ('                                  ')
    print ('**********************************')


tic_tac_board(board)

player_one = 'X'
player_two = 'O'
input_ppl = input("Choose player X or 0: ").upper()
if input_ppl == 'X':
    player_one = 'X'
    player_two = 'O'
else:
    player_one = 'O'
    player_two = 'X'
    
print('Player one: %s \nPlayer two: %s' %(player_one, player_two))
print ('**********************************')
print('*********Start the Game************')
print ('**********************************')

