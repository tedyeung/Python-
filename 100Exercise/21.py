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

