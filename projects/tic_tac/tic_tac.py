# plyers
print ('Wellcome to Tic Tac Toe Game by Slavo7')
print ('***************************************')
player_one = input("Please choose, use caplital letters: X or O): ")
player_two = None
def ppl():
    if player_one == 'O':
         player_two = 'X'
         return player_two
    else:
        return player_two
ppl()
print ('Player one is %s, player two is %s' %(player_one, player_two))