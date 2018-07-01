import random

print('Find Number from 0 to 10')

random_number = random.randint(0,10)
game = True

while game:
    number = input('Please add number: ')
    num = int(number)
    if random_number == num:
        print('Well Done you found the number')
        game = False
    else: 
        print('Like number is: ', random_number)