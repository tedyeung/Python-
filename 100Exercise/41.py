'''
Question: Create a script that generates a text file with all letters of English alphabet inside it, one letter per line.
'''

from string import ascii_lowercase

alph = ascii_lowercase

def alph_file(data):
    with open('41.txt', 'w') as f:
        for a in data:
            f.write(a + '\n')

alph_file(alph)
        
