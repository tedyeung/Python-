# while loop
wishes = []
question = 'Please enter your wishes: '
while question != 'Quit':
    question = input(question)
    wishes.append(question)

print (wishes)
print('\n', '****************************', '\n')