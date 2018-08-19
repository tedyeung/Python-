'''
Question: Create a script that generates a file where all letters of English alphabet are listed two in each line. The inside of the text file would look like:

ab
cd
ef

and so on.
'''

from string import ascii_lowercase
a = ascii_lowercase[::2]
b = ascii_lowercase[1::2]

with open('43.txt', 'w') as f:
    for x,y in zip(a,b):
        f.write(x + y + '\n')
 

