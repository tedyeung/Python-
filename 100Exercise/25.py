# print from a to z all letters 

from string import ascii_letters
from string import ascii_lowercase
import re

a = ascii_letters
b = ascii_lowercase

match = re.findall(r'[A-Z]', a)

print(b)



