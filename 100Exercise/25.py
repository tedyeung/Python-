# print from a to z all letters 

from string import ascii_letters
from string import ascii_lowercase
import re

a = ascii_letters
b = ascii_lowercase

comp = re.compile(r'^[A-Z\d]')

print(comp.match(a))

for letter in a:
    if (comp == letter):
        print(letter)
# a = a.replace(comp, '!!')
# a = a.replace(match, '!')



