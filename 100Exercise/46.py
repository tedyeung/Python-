'''
Question: Please create a script that generates 26 text files named a.txt, b.txt, and so on up to z.txt. Each file should contain a letter reflecting its filename. So, a.txt will contain letter a, b.txt will contain letter b and so on
'''

from string import ascii_lowercase


for letter in ascii_lowercase:
    with open("46" + "/" + letter + '.txt', "w") as f:
        f.write('I love Python, Matematics and Programing')