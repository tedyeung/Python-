# Make a dict wich will print a , b , c list of 1 - 30
from pprint import pprint
d = {
    "a": list(range(1,11)), 
    "b": list(range(10,21)),
    "c": list (range(21,31))
}

pprint(d)