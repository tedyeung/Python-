# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}
b = {}
# Expected output:  {'a': 1}  

for key in d:
    if (d[key] > 1):
        pass
    else: 
        b[key] = d[key]
    
print (b)

# solution 2

aff = {"a": 1, "b": 2, "c": 3}
aff = dict((key, value) for key, value in aff.items() if value <= 1)
print(aff)