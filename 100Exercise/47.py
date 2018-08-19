# check if letters inside the text file blongs to pyhton word

from string import ascii_lowercase

ascii_string = ascii_lowercase
name = 'python'
python_letter_list = []

for char in ascii_string:
    for letter in name:
        with open("46" + '/' + char + ".txt", 'r') as f:
            data = f.read()
        if(data == letter):
            python_letter_list.append(letter)


print('Result: ',python_letter_list)

'''
2 Solution
import glob
 
letters = []
file_list = glob.iglob("46/*.txt")
check = "python"
 
for filename in file_list:
    with open(filename,"r") as file:
        letter = file.read().strip("\n")
        if letter in check:
            letters.append(letter)
 
print(letters)

'''