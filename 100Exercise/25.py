# print from a to z all letters 

from string import ascii_letters
from string import ascii_lowercase
import re

a = ascii_letters
b = ascii_lowercase

match = re.search(r"[A-Z]", a)

# a = a.replace(match, '!')
print(match)
# print(a)
print (b)
for letter in a:
    if (letter == match):
        print(letter)
