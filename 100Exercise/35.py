'''
Create a function that takes any string as input and returns the number of words for that string.
'''

some_input = input("How are you? ")

def some_str_number(some_string):
    split_string = some_string.split(" ")
    return(len(split_string))



print(some_str_number(some_input))