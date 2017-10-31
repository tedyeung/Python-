# while loop
wishes = []
question = 'Please enter your wishes: '
answer = ""
while answer != 'Quit':
    answer = input(question)
    if answer != 'Quit':
        wishes.append(answer)
    else:
        print('Start NOW!!!')

print(wishes)
print('\n', '****************************', '\n')

question = ('How old are you? ')
answer = ''
active = True

while active:
    answer = input(question)
    if answer == 'quit':
        active = False
    elif int(answer) < 3:
        print('For Babies tickets are free!!!')
    elif int(answer) == 3:
        print('Your ticket is %80 discount')
    elif int(answer) <= 18:
        print('You ticket is %50')
    elif int(answer) > 18:
        print('You are paying full price')

print ('Thank you for buying tickets!!!')
        
        
        