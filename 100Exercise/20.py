# Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}
# Expected output: 6

def dicSum(d):
    l=[]
    for a in d:
        l.append(d[a])
    return sum(l)

print("Sum of dic:", dicSum(d))