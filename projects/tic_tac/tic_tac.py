print ('WELCOME TO TIC TAC TOE GAME ENJOY')
print ('**********************************')
print ('                                  ')

def winner():
    if board[1] == board[2] == board [3]:
        print("Well done %s you are the best" %(board[1]))
    elif board[4] == board[5] == board [6]:
        print("Well done %s you are the best" %(board[4]))
    elif board[7] == board[8] == board [9]:
        print("Well done %s you are the best" %(board[7]))
    elif board[1] == board[5] == board [9]:
        print("Well done %s you are the best" %(board[1]))
    elif board[3] == board[5] == board [7]:
        print("Well done %s you are the best" %(board[3]))
    else:
        pass
              

def top_title():
    print('************************')
    print('New Move')
    print('Chose the left positions')

board = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def tic_tac_board (board):
    print (' ' + board[1] + '|' + board[2] + '|' + board[3] + " ")
    print ("-------")
    print (' ' + board[4] + '|' + board[5] + '|' + board[6] + " ")
    print ('-------')
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
elif input_ppl == 'O':
    player_one = 'O'
    player_two = 'X'
else:
    print ('You add wrong parametar and Player one: X, Player two: O')
    
print('Player one: %s \nPlayer two: %s' %(player_one, player_two))
print ('**********************************')
print('*********Start the Game************')
print ('**********************************')
def ppl_moves():
    add_one = int(input('Player one - please add %s in position from 1 to 9: ' %(player_one)))
    add_two = int(input('Player one - please add %s in position from 1 to 9: ' %(player_two)))
    board[add_one] = player_one
    board[add_two] = player_two
    return(board)
ppl_moves()
tic_tac_board(board)

top_title()
ppl_moves()
tic_tac_board(board)

top_title()
ppl_moves()
tic_tac_board(board)
winner()


top_title()
ppl_moves()
tic_tac_board(board)
winner()

top_title()
ppl_moves()
tic_tac_board(board)
winner()