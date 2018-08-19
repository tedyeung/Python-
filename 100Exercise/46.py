# Make a list from the the text files 

from string import ascii_lowercase

alph_list = []

for char in ascii_lowercase:
    with open("46/" + char + ".txt", 'r') as f:
        data = f.read()
    alph_list.append(data)

print("Data List: ", alph_list)