'''
Question: Create a script that generates a file where all letters of English alphabet are listed three in each line. The inside of the text file would look like:

abc
def
ghi

and so on.
'''
from string import ascii_lowercase

a = ascii_lowercase[::3]
b = ascii_lowercase[1::3]
c = ascii_lowercase[2::3]

print(a + '\n' + b + '\n' + c)

with open('44.txt', 'w') as f:
    for x,y,z in zip(a,b,c):
        f.write(x + y + z + '\n')

