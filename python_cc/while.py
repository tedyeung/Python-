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