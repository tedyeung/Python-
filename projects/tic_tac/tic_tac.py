# plyers
print ('Wellcome to Tic Tac Toe Game by Slavo7')
print ('***************************************')
player_one = input("Please choose, use caplital letters: X or O): ")
def ppl():
    player_two = 'O'
    if player_one == 'O':
         return 'X'
    else:
        return 'O'
player_two = ppl()
print ('Player one is %s, player two is %s' %(player_one, player_two))

def drawBoard(board):
    # This function prints out the board that it was passed.
    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


drawBoard(board)