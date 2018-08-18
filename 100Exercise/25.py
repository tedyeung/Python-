# print from a to z all letters 

from string import ascii_letters
from string import ascii_lowercase
import re

a = ascii_letters
b = ascii_lowercase

match = re.match("\W[A-Z]|", a)
print(match)





