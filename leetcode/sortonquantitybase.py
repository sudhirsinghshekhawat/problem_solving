from collections import Counter

arr = [5, 4, 5, 5, 6, 3, 6, 2, 4]

d = {1: 2, 11: 1, 45: 3}

d = {k: v for k, v in sorted(d.items(), key=lambda x: x[1])}
res = []
result = [[k] * v for k, v in sorted(dict(Counter(arr)).items(), key=lambda x: x[1])]
for val in result:
    res.extend(val)
print(res)
