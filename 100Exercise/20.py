# Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}
# Expected output: 6
l = []
for a in d:
    l.append(d[a])

print(sum(l))