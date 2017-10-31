# while loop
wishes = []
question = 'Please enter your wishes: '
answer = ""
while answer != 'Quit':
    answer = input(question)
    wishes.append(answer)

print(wishes)

print('\n', '****************************', '\n')