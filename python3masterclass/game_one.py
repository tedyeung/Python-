import random

print('Find Number from 0 to 10')

random_number = random.randint(0,10)

num = int(number)

while random_number == num:
    number = input('Please add number: ')
    if random_number == num:
        print('Well Done you found the number')
        break
    else: 
        print('Like number is: ', random_number)