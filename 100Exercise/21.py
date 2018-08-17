# Question: Filter the dictionary by removing all items with a value of greater than 1.

d = {"a": 1, "b": 2, "c": 3}

# Expected output:  {'a': 1}  

for keys in d:
    if (d[keys] > 1):
        print(d[keys]>1)
    else: 
        print(False)
    
print (d)

