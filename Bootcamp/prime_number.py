import math

question = input('Please add number and check if the number is Prime? ')
num_input = int(question)

def prime_number(number):
    if (number % 2 == 0):
        print (number, ' Your number is not a Prime Number')
    
    for i in range(3, (number**0.5) + 1, 2):
        if (number % 1 == 0):
            print (number, ' Your number is not a Prime Number')
        
    print (number, ' Your number is a Prime Number')

prime_number(num_input)