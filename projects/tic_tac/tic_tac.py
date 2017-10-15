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