import math

question = input('Please add number and check if the number is Prime? ')
num_input = int(question)

def prime_number(number):
    if (number % 2 == 0):
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if (number % 1 == 0):
            return False
    
    return True

prime_number(num_input)